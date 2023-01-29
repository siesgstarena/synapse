import os
import pandas as pd
from flask import Blueprint, request, jsonify
from helper.problem.poc import raw, prepro, train_knn, save_similarities
from services.problem.save_db import save_db
from utils import upload_file_to_firebase, send_mail

index = Blueprint(name="training", import_name=__name__)


@index.route("", methods=["POST"])
def training_handler():
    try:
        json = request.get_json()
        data = json["data"]
        submission_path = raw(data)
        submission_df = pd.read_csv(f"./{submission_path}")
        x = prepro(submission_df)
        sucess_score_path = "success_score.csv"
        x.to_csv(f"./{sucess_score_path}")
        df = pd.read_csv(f"./{sucess_score_path}")
        df.rename(columns={"Unnamed: 0": "problemId"}, inplace=True)
        model_path = "knn_ball_tree.pkl"
        train_knn(df, len(df["problemId"]) - 1, "ball_tree", model_path)
        similarities_path = "similarities.pkl"
        save_similarities(
            df, len(df["problemId"]) - 1, "knn_ball_tree.pkl", similarities_path
        )
        paths = upload_file_to_firebase(
            "problem",
            [submission_path, sucess_score_path, model_path, similarities_path],
        )
        model = save_db(paths)
        response = {
            "status": "success",
            "message": "Training completed",
            "similarities_path": f"./{similarities_path}",
            "model_path": f"./{model_path}",
            "sucess_score_path": f"./{sucess_score_path}",
            "submission_path": f"./{submission_path}",
            "paths": paths,
            "model": model,
        }
        send_mail(
            os.environ.get("MAIL_USERNAME"),
            "Training Completed",
            str(response),
        )

        return jsonify(
            {
                "status": "success",
                "message": "Training completed",
            }
        )

    except Exception as e:
        print(e)
        send_mail(
            os.environ.get("MAIL_USERNAME"),
            "Training Failed",
            str(e),
        )
        return jsonify({"status": "error", "message": str(e)})

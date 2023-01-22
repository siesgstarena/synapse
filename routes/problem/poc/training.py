import pandas as pd
from flask import Blueprint, request, jsonify
from helper.problem.poc import raw, prepro, train_knn, save_similarities
from utils.backup.firebase import upload_file_to_firebase
from services.problem.save_db import save_db

index = Blueprint(name="training", import_name=__name__)


@index.route("", methods=["POST"])
def training_handler():
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
    train_knn(df, 3, "ball_tree", model_path)
    similarities_path = "similarities.pkl"
    save_similarities(df, 3, "knn_ball_tree", similarities_path)
    paths = upload_file_to_firebase(
        "problem", [submission_path, sucess_score_path, model_path, similarities_path]
    )
    model = save_db(paths)
    return jsonify(
        {
            "status": "success",
            "message": "Training completed",
            "similarities_path": f"./{similarities_path}",
            "model_path": f"./{model_path}",
            "sucess_score_path": f"./{sucess_score_path}",
            "submission_path": f"./{submission_path}",
            "paths": paths,
            "model": model,
        }
    )

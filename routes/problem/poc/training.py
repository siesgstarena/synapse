import pandas as pd
from flask import Blueprint, request
from helper.problem.poc import raw, prepro, train_knn, save_similarities

index = Blueprint(name="training", import_name=__name__)


@index.route("", methods=["GET"])
def indexs():
    json = request.get_json()
    data = json["data"]
    submission_path = raw(data)
    submission_df = pd.read_csv(f"./{submission_path}")
    x = prepro(submission_df)
    x.to_csv("./success_score.csv")
    df = pd.read_csv("./success_score.csv")
    df.rename(columns={"Unnamed: 0": "problemId"}, inplace=True)
    train_knn(df, 3, "ball_tree", "knn_ball_tree")
    save_similarities(df, 3, "knn_ball_tree")
    return "DOne"

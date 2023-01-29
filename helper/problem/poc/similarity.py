from collections import defaultdict
import pandas as pd
import numpy as np
from utils import load_model, save_model as save_sim

# pylint: disable=redefined-outer-name


def knn_recommend(problem_id, n_neighbors, df, knn):
    Y = df["problemId"]
    to_predict = np.array(
        df[df["problemId"] == problem_id].drop("problemId", axis=1)
    ).reshape(1, -1)
    _, indices = knn.kneighbors(to_predict, n_neighbors=n_neighbors)
    rec = []
    for i in indices[0]:
        if Y.iloc[i] != problem_id:
            rec.append(Y.iloc[i])
    return rec


def save_similarities(df, n_neighbors, model_name, similarities_path):
    knn = load_model(model_name)
    sim = defaultdict(list)
    for j in df["problemId"]:
        sim[j].append(knn_recommend(j, n_neighbors, df, knn))
    save_sim(sim, similarities_path)


if __name__ == "__main__":
    df = pd.read_csv("./success_score.csv")
    df.rename(columns={"Unnamed: 0": "problemId"}, inplace=True)
    sim = defaultdict(list)
    for j in df["problemId"]:
        sim[j].append(knn_recommend(j, 3, df, load_model("knn_ball_tree")))
    save_sim(sim, "similarities.pkl")

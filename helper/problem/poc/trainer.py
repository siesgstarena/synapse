import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
from utils.save_model import save_model

# pylint: disable=redefined-outer-name


def train_knn(df, n_neighbors, algorithm, model_name):
    X = df.drop("problemId", axis=1)
    Y = df["problemId"]
    knn = KNN(n_neighbors=n_neighbors, algorithm=algorithm)
    knn.fit(X, Y)
    save_model(knn, model_name)


if __name__ == "__main__":
    df = pd.read_csv("./data/processed/success_score.csv")
    df.rename(columns={"Unnamed: 0": "problemId"}, inplace=True)
    # n = random.randint(0, 9)
    n = 3
    train_knn(df, n, "ball_tree", "knn_ball_tree")

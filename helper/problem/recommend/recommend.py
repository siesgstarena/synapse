from utils import load_model


def recommend(problem_id):
    sim = load_model("similarities.pkl")
    return sim[problem_id]


if __name__ == "__main__":
    print(recommend("5b5c8cd7276e2200208fed62"))

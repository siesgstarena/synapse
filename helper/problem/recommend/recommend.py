from firebase_admin import storage
from utils import load_model
from services.problem.load_model import load_current_model


def recommend(problem_id):
    model = load_current_model()
    current_date = model.date
    bucket = storage.bucket()
    blob = bucket.blob(f"problem/{current_date}/similarities.pkl")
    blob.download_to_filename("similarities.pkl")
    sim = load_model("similarities.pkl")
    return sim[problem_id]


if __name__ == "__main__":
    print(recommend("5b5c8cd7276e2200208fed62"))

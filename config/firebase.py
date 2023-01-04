import os
import json
import firebase_admin
from firebase_admin import credentials

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, "arena-recomendation-firebase.json")

with open(file, encoding="utf-8") as f:
    data = json.load(f)
data["private_key"] = os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n")

cred = credentials.Certificate(data)

firebase_admin.initialize_app(
    cred, {"storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET")}
)

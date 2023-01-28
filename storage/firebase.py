import os
import json
import firebase_admin
from firebase_admin import credentials


def init_firebase():
    flask_env = os.environ.get("FLASK_ENVIRONMENT")
    file_name = (
        "synapse-dev.json" if flask_env == "development" else "synapse-prod.json"
    )
    private_key = (
        os.environ.get("FIREBASE_PRIVATE_KEY_DEV")
        if flask_env == "development"
        else os.environ.get("FIREBASE_PRIVATE_KEY_PROD")
    )
    storage_bucket = (
        os.environ.get("FIREBASE_STORAGE_BUCKET_DEV")
        if flask_env == "development"
        else os.environ.get("FIREBASE_STORAGE_BUCKET_PROD")
    )
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, file_name)

    with open(file, encoding="utf-8") as json_file:
        data = json.load(json_file)
    data["private_key"] = private_key.replace("\\n", "\n")

    cred = credentials.Certificate(data)

    firebase_admin.initialize_app(cred, {"storageBucket": storage_bucket})

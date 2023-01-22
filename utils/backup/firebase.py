import os
from datetime import datetime
from firebase_admin import storage


def upload_file_to_firebase(type_name, file_paths):
    bucket = storage.bucket()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    firebase_url = []
    for file_path in file_paths:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, f"../../{file_path}")
        blob = bucket.blob(f"{type_name}/{current_date}/{file_path}")
        blob.upload_from_filename(filename)
        blob.make_public()
        firebase_url.append(blob.public_url)
    firebase_url.append(current_date)
    return firebase_url

import os
from flask import Blueprint
from firebase_admin import storage
from models.problem import ProblemModel

index = Blueprint(name="index", import_name=__name__)


@index.route("", methods=["GET"])
def indexs():
    return "Hello World"


@index.route("/firebase", methods=["GET"])
def firebases():
    # upload t.csv to firebase
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, "t.csv")
    bucket = storage.bucket()
    blob = bucket.blob("t.csv")
    blob.upload_from_filename(file)
    return "Hello World"


@index.route("/firebase/folder", methods=["GET"])
def firebase_folder():
    # upload t.csv to a folder of name current date
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, "t.csv")
    bucket = storage.bucket()
    blob = bucket.blob("2020-05-01/t.csv")
    blob.upload_from_filename(file)
    return "Hello World"


@index.route("/mongo", methods=["GET"])
def mongo():
    # save a model to mongo
    model = ProblemModel(
        raw_dataset_url="https://raw_dataset_url",
        processed_dataset_url="https://processed_dataset_url",
        model_url="https://model_url",
    )
    model.save()
    return "Hello World"

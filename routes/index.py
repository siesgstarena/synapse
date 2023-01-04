from flask import Blueprint
index = Blueprint(name="index", import_name=__name__)
from firebase_admin import storage
import os
@index.route('', methods=['GET'])
def indexs():
    return "Hello World"

@index.route('/firebase',methods=['GET'])
def firebases():
    # upload t.csv to firebase
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 't.csv')
    bucket = storage.bucket()
    blob = bucket.blob('t.csv')
    blob.upload_from_filename(file)
    return "Hello World"

@index.route('/firebase/folder',methods=['GET'])
def firebase_folder():
    # upload t.csv to a folder of name current date
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 't.csv')
    bucket = storage.bucket()
    blob = bucket.blob('2020-05-01/t.csv')
    blob.upload_from_filename(file)
    return "Hello World"
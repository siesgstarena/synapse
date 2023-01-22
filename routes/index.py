from flask import Blueprint

index = Blueprint(name="index", import_name=__name__)


@index.route("", methods=["GET"])
def indexs():
    return "<h1> Offcial Arena: Recommendation System <br> <a href='/admin/login'>Login</a></h1>"

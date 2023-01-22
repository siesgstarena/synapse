from flask import Blueprint, render_template

index = Blueprint(name="index", import_name=__name__)


@index.route("", methods=["GET"])
def index_handler():
    return render_template("index.html")

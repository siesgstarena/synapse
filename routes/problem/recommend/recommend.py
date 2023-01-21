from flask import Blueprint, request
from helper.problem.recommend import recommend

index = Blueprint(name="recommend", import_name=__name__)


@index.route("", methods=["GET"])
def indexs():
    json = request.get_json()
    data = json["data"]
    problem_id = data["id"]
    return recommend(problem_id)

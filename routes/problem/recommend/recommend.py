import os
from flask import Blueprint, request, jsonify
from helper.problem.recommend import recommend
from utils.send_mail import send_mail

index = Blueprint(name="recommend", import_name=__name__)


@index.route("", methods=["GET"])
def recommend_handler():
    try:
        json = request.get_json()
        data = json["data"]
        problem_id = data["id"]
        return recommend(problem_id)
    except Exception as e:
        send_mail(
            os.environ.get("MAIL_USERNAME"),
            "Training Failed",
            str(e),
        )
        return jsonify({"status": "error", "message": str(e)})

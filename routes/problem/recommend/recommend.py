import os
from collections import Counter
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
        already_solved = data["solved"]
        similar = recommend(problem_id)
        intersection = Counter(similar[0]) & Counter(already_solved)
        will_recommend = list(Counter(similar[0]) - intersection)
        return will_recommend[:3] if len(will_recommend) >= 3 else will_recommend
    except Exception as e:
        send_mail(
            os.environ.get("MAIL_USERNAME"),
            "Recommendation Error",
            str(e),
        )
        return jsonify({"status": "error", "message": str(e)})

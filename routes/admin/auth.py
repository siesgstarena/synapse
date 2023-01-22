import os
from flask import Blueprint, render_template, request, session, redirect

index = Blueprint(name="auth", import_name=__name__)


@index.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    username = request.form.get("username")
    password = request.form.get("password")
    if username == os.environ.get("ADMIN_USERNAME") and password == os.environ.get(
        "ADMIN_PASSWORD"
    ):
        session["admin"] = True
        return redirect("/admin")
    return redirect("/admin/login")


@index.route("/logout", methods=["GET"])
def logout():
    session["admin"] = False
    return redirect("/")

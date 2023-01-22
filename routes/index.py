import os
from flask import Blueprint, request, render_template, redirect, url_for
from firebase_admin import storage
from models.problem import ProblemModel
from models.user import LoginForm, RegistrationForm, User
import flask_login as login
index = Blueprint(name="index", import_name=__name__)


# @index.route("", methods=["GET"])
# def indexs():
#     return "Hello World"


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
@index.route('/', methods=["GET"])
def home():
    return render_template('index.html', user=login.current_user)

@index.route('/login/', methods=('GET', 'POST'))
def login_view():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.get_user()
        login.login_user(user)
        return redirect(url_for('index.home'))

    return render_template('form.html', form=form)


@index.route('/register/', methods=('GET', 'POST'))
def register_view():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()

        form.populate_obj(user)
        print(user)
        user.save()

        login.login_user(user)
        return redirect(url_for('index.home'))

    return render_template('form.html', form=form)


@index.route('/logout/')
def logout_view():
    login.logout_user()
    return redirect(url_for('index.home'))
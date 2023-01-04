from routes.index import index

# pylint: disable=unused-import
# flake8: noqa
from . import firebase


def create_app(app):
    app.register_blueprint(index, url_prefix="/")
    return app

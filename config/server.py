from routes.index import index

from db.mongo import init_mongo
from storage.firebase import init_firebase


def create_app(app):
    init_firebase()
    app = init_mongo(app)
    app.register_blueprint(index, url_prefix="/")
    return app

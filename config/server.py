from routes.index import index
from routes.problem.poc.training import index as training
from routes.problem.recommend.recommend import index as recommend
from db.mongo import init_mongo
from storage.firebase import init_firebase


def create_app(app):
    init_firebase()
    app = init_mongo(app)
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(training, url_prefix="/problem/training")
    app.register_blueprint(recommend, url_prefix="/problem/recommend")
    return app
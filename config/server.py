import flask_admin as admin
from models.problem import ProblemModel, ProblemView
from routes.index import index
from routes.problem.poc.training import index as training
from routes.problem.recommend.recommend import index as recommend
from db.mongo import init_mongo
from storage.firebase import init_firebase
import flask_login as login
import models.user as User
def init_login(app):
    login_manager = login.LoginManager()
    login_manager.setup_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.User.objects(id=user_id).first()
# Create customized index view class
class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated


def create_app(app):
    init_firebase()
    app = init_mongo(app)
    init_login(app)
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(training, url_prefix="/problem/training")
    app.register_blueprint(recommend, url_prefix="/problem/recommend")
    admins = admin.Admin(
        app, "Arena: Recommendation System", template_mode="bootstrap4",index_view=MyAdminIndexView()
    )
    admins.add_view(ProblemView(ProblemModel))
    return app

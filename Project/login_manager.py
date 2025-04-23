import flask_login
from .settings import project
from authorization_app import User

project.secret_key = "secret_key"
login_manager = flask_login.LoginManager(app = project)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
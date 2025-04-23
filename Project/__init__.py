from .urls import *
from .db import DATABASE, MIGRATE
from .settings import project
from .login_manager import *
from .loadenv import execute

import authorization_app.models

project.register_blueprint(blueprint = home_app.home)
project.register_blueprint(blueprint = authorization_app.login)
project.register_blueprint(blueprint = authorization_app.authorization)
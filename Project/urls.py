import home_app
import authorization_app
from .settings import project

home_app.home.add_url_rule(
    rule = "/", #/ - головна стоірнка
    view_func= home_app.render_home #
)

authorization_app.login.add_url_rule(
    rule = "/login", 
    view_func= authorization_app.render_login,
    methods= ["GET", "POST"] 
)

authorization_app.authorization.add_url_rule(
    rule = "/authorization", 
    view_func= authorization_app.render_authorization,
    methods= ["GET", "POST"] 
)


project.register_blueprint(blueprint = home_app.home)
project.register_blueprint(blueprint = authorization_app.login)
project.register_blueprint(blueprint = authorization_app.authorization)
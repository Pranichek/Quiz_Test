import flask

#
login = flask.Blueprint(
    name = "login",#
    import_name = "authorization_app",#
    template_folder = "templates",#
    static_folder = "static",#
    static_url_path = "/login/static/"#
)

#
authorization = flask.Blueprint(
    name= "authorization",#
    import_name= "authorization_app",#
    template_folder= "templates",#
    static_folder= "static",#
    static_url_path= "/authorization/static/"#
)
import flask

#
home = flask.Blueprint(
    name = "home", # 
    import_name = "home_app", #
    static_url_path = "/static/", #
    static_folder = "static", #
    template_folder = "templates" #
)
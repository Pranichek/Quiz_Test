import flask
import home_app

#
project = flask.Flask(
    import_name = "Project", #
    static_folder ="static", # 
    template_folder = "templates", # 
    static_url_path = "/static/" #
)

#
project.register_blueprint(blueprint= home_app.home)

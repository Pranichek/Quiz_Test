import os
import flask
import flask_sqlalchemy
import flask_migrate


project = flask.Flask(
    import_name = "Project", 
    static_folder ="static",  
    template_folder = "templates",  
    static_url_path = "/static/", 
    instance_path = os.path.abspath(os.path.join(__file__, "..", "instance"))
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"


DATABASE = flask_sqlalchemy.SQLAlchemy(app= project)
MIGRATE = flask_migrate.Migrate(
    app = project, 
    db = DATABASE, 
    directory = os.path.abspath(os.path.join(__file__, "..", "migrations"))
)
import os
import flask

project = flask.Flask(
    import_name = "Project", 
    static_folder ="static",  
    template_folder = "templates",  
    static_url_path = "/static/", 
    instance_path = os.path.abspath(os.path.join(__file__, "..", "instance"))
)


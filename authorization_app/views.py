import flask
from .models import User
from Project.db import DATABASE
from flask_login import current_user, login_user

def render_authorization():
    #
    if flask.request.method == "POST":
        try:
            #
            user = User(
                name = flask.request.form["name"],
                surname = flask.request.form["surname"],
                username = flask.request.form["username"],
                email = flask.request.form["email"],
                password = flask.request.form["password"]
            )
            #
            DATABASE.session.add(user)
            #
            DATABASE.session.commit()
            #
            return flask.redirect("/")
        except Exception as error:
            print(f"Error: {error}")

    #
    return flask.render_template(template_name_or_list="authorization.html")

#
def render_login():
    if isinstance(current_user, User):
        return flask.redirect("/")
                  
    if flask.request.method == "POST":
        try:
            # отримуємо всіх користувачів з бази даних
            users = User.query.all()
            #
            for user in users:
                #
                if user.username == flask.request.form["username"] and user.password == flask.request.form["password"]:
                    login_user(user)
                    return flask.redirect("/")
        except Exception as error:
            print(f"Error: {error}")
    #
    return flask.render_template(template_name_or_list="login.html")
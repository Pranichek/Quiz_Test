from Project.settings import DATABASE
#
import flask_login

#
class User(DATABASE.Model, flask_login.UserMixin):
    #
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, nullable = False)

    name = DATABASE.Column(DATABASE.String(80), nullable = False)
    surname = DATABASE.Column(DATABASE.String(80), nullable = False)
    username = DATABASE.Column(DATABASE.String(80), unique = True, nullable = False)
    email = DATABASE.Column(DATABASE.String(120), unique = True, nullable = False)
    password = DATABASE.Column(DATABASE.String(120), nullable = False)
    is_mentor = DATABASE.Column(DATABASE.Boolean)

    #DATABASE.String(80) - 
    #nullable = False - 
    #unique = True - 
    #DATABASE.Boolean - 

    # метод для отримання нікнейму користувача
    def __repr__(self):
        return f"<User {self.username}>"
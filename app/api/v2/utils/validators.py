from werkzeug.security import check_password_hash
from ..models.user_models import USERS
from instance.config import Config
from functools import wraps
from ..models import user_models
from  flask import request, json, jsonify, make_response
import re, jwt

users = user_models.UserModels()
SECRET_KEY = Config.JWT_SECRET_KEY

class Validations():
    def __init__(self):
        self.users = USERS

    def validate_password(self, password):
        exp = "^[a-zA-Z0-9@_+-.]{3,}$"
        return re.match(exp, password)

    def validate_email(self, email):
        exp = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)"
        return re.match(exp, email)
	#Check login creds...
    def email_correct(self, email):
        usr = [user for user in self.users if user['email'] == email]
        if usr:
            return True
        else:
            return False


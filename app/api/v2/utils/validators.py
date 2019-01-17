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
        exp = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(exp, email)
	#Check login creds...
    def email_correct(self, email):
        usr = [user for user in self.users if user['email'] == email]
        if usr:
            return True
        else:
            return False

    def same_password(self, email, password):
        usr = [user for user in self.users if user['email'] == email]
        if usr:
            validate = check_password_hash(usr['password'], password)
            if validate:
                return True
            else:
                return False

    def email_exists(self, email):
        usr = [user for user in self.users if user['email'] == email]
        if usr:
            return True
        else:
            return False

def auth_required(func):
    """ validation decorator. Validates if user is logged in before performing a task """
    @wraps(func)
    def decorator_func(*args, **kwargs):
        auth_token = None
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split("Bearer ")[1]
     
        if not auth_token:
            return make_response(jsonify({
                "status": 401,
                "data": "Unauthorized! Token required"
            })), 401
        try:
            response = users.verify_auth_token(auth_token)
            if isinstance(response, str):
                user = users.login(username=response)
                if not user:
                    return make_response(jsonify({
                        "status": 400,
                        "message": "Authentication failed: Wrong username"
                    })), 400
        except:
            return make_response(jsonify({
                "status": 400,
                "message": "Authentication failed: Invalid token"
            })), 400
        return func(user, *args, *kwargs)
    return decorator_func


def requires_admin(func):
    """ validation decorator. Validates if user is logged in before performing a task """
    @wraps(func)
    def decorator_func(*args, **kwargs):
        auth_token = None
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split("Bearer ")[1]
        # else:
        #     return make_response(jsonify({
        #         "status": 401,
        #         "message": "Authentication header missing"
        #     }))
        if not auth_token:
            return make_response(jsonify({
                "status": 401,
                "data": "Unauthorized! Token required"
            })), 401
        try:
            response = users.verify_auth_token(auth_token)
            if isinstance(response, str):
                user = users.login(username=response)
                if not user:
                    return make_response(jsonify({
                        "status": 400,
                        "message": "Authentication failed: Wrong username"
                    })), 400
                is_admin = user[7]
                if is_admin != "True":
                    return make_response(jsonify({
                        "status": 400,
                        "message": "Authentication failed: Not Admin"
                    })), 400
        except:
            return make_response(jsonify({
                "status": 400,
                "message": "Authentication failed: Invalid token"
            })), 400
        return func(user, *args, *kwargs)
    return decorator_func

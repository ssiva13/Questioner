from flask import Flask, Blueprint, jsonify, request, make_response
from ..models.user_models import UserModels
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.validators import Validations

import jwt, secrets


user_v2 = Blueprint("usersv2", __name__, url_prefix='/api/v2')

validator = Validations()
#users = user_models.UserModels()


@user_v2.route('/auth/signup', methods=['POST'])
def register():
    """ A view to control creation of users """

    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400

    Name = data.get('Name')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    userName = data.get('userName')
    isAdmin = data.get('isAdmin')
    password = data.get('password')

    if not Name:
        return make_response(jsonify({
            "status": 400,
            "message": "Name is required"
        })), 400
    if not email:
        return make_response(jsonify({
            "status": 400,
            "message": "email is required"
        })), 400
    if not phoneNumber:
        return make_response(jsonify({
            "status": 400,
            "message": "Phone number is required"
        })), 400
    if not userName:
        return make_response(jsonify({
            "status": 400,
            "message": "Username is required"
        })), 400
    if not password:
        return make_response(jsonify({
            "status": 400,
            "message": "Password is required"
        })), 400

    if not validator.validate_email(email):
        return make_response(jsonify({
            "status": 400,
            "message": "Invalid email"
        })), 400


    password = generate_password_hash(
        password, method='pbkdf2:sha256', salt_length=2)
    

    user = UserModels()
    uers =user.signup(Name, email, phoneNumber, userName, isAdmin, password )
    if uers:
	    status = uers[1]
	    data = uers[0]
	    auth_token = user.generate_token(email)
	    
	    return make_response(jsonify( {"status": status, "User Data": data, "token":auth_token} )), status
    return None



@user_v2.route('/auth/login', methods=['POST'])
def login():
    """ A view to control users login """
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400
    email = data.get('email')
    password = data.get('password')

    if not email:
        return make_response(jsonify({
            "status": 400,
            "message": "Username is required"
        })), 400
    if not password:
        return make_response(jsonify({
            "status": 400,
            "message": "Password is required"
        })), 400
    if not validator.validate_email(email):
        return make_response(jsonify({
            "status": 400,
            "message": "Invalid email"
       })), 400

    

    users = UserModels()
    user_logged =users.login(email)
    
    if user_logged:
        if check_password_hash(user_logged[1], password):
            auth_token = users.generate_token(email)
            return make_response(jsonify({
                "status": 200,
                "User Email": user_logged[0],
                "User Password": user_logged[1],
                "token": auth_token
            })), 200
        return make_response(jsonify({
            "status": 400,
            "message": "Incorrect password"
        })), 400
    
    return make_response(jsonify({
        "status": 404,
        "message": "User does not exist. Register??"
    })), 404



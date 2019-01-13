from flask import Blueprint, jsonify, make_response, request, json
from ..models.user_models import UserModel
from ..models.user_models import USERS

users_bp = Blueprint("users", __name__, url_prefix="/api/v1/")


@users_bp.route("/", methods=["GET"])
def home():
	return "This is Home" 
	


@users_bp.route("/users/", methods=["POST"])
def add_user():
	registeredOn = request.json["registeredOn"]
	Name = request.json["Name"]
	email = request.json["email"]
	userName = request.json["userName"]
	password = (request.json["password"])
	phoneNumber = request.json["phoneNumber"]
	isAdmin = request.json["isAdmin"]

	"""Checking User Details"""
	if not Name or not email or not userName or not phoneNumber or not password or not isAdmin:
		return make_response(jsonify({
				"status": 400,
				"message": "Please fill in all required details"
			})), 400
	else:
			"""If all fields are filled"""
			user = UserModel(Name, registeredOn, email, userName, password, phoneNumber, isAdmin)
			user_reg = user.create_user()
			return make_response(jsonify({
				"status" : 201,
				"USERS": user_reg
			})), 201


@users_bp.route("/users/auth/", methods=['POST'])
def user_login():
	email = request.json["email"]
	password = (request.json["password"])
	

	"""Check user credentials"""
	if not password:
		return make_response(jsonify({
			"status": 400,
			"message": "please input your password"
		})), 400
		
	if not email:
			return make_response(jsonify({
			"status": 400,
			"message": "please input your email"
		})), 400
	if len(USERS) != 0:
		user_logged = UserModel.login_user(email, password)

		""" IF any exists"""
		try:
			"""Check if password and email match"""
			if email == user_logged["email"] and password == user_logged["password"]:
				return make_response(jsonify({
					"status": 200,
					"USER" : user_logged
					})), 200
		except:
			return make_response(jsonify({
					"status": 401,
					"USER" : "Wrong email and/or Password"
					})), 401
		
	else:
		return make_response(jsonify({
			"status": 404,
			"message": "No Users In Database"
		})), 404
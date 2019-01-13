import unittest, pytest, datetime, json, instance
from datetime import date
from flask import current_app, Flask,  request
from run import app
from app.api.v1.views import user_views
from app.api.v1.models import user_models
from app.api.v1.views.user_views import users_bp



class BaseUserTest(unittest.TestCase):

	def setUp(self):
		self.app = app
		self.client = self.app.test_client()

		self.user1 = {
				"registeredOn":"",
				"Name": "Simon Siva",
				"email":"sudi",
				"userName": "simftgon",
				"phoneNumber":"908374647",
				"password":"4fgrct745",
				"isAdmin": True
		}
		self.user2 = {
				"registeredOn":"",
				"Name": "Simon Siva",
				"email":"sudi",
				"userName": "",
				"phoneNumber":"908374647",
				"password":"4fgrct745",
				"isAdmin": True
		}
		self.user3 = {
				"email":"sudi",
				"password":"4fgrct745"
		}
		self.user4 = {
				"email":"",
				"password":"4fgrct745"
		}
		self.user5 = {
				"email":"sudi",
				"password":""
		}

	def tearDown(self):
		pass

class TestUsers(BaseUserTest):
	def test_create_user(self):
		today_now =  date.today()
		response = self.client.post("/api/v1/users/", data = json.dumps(self.user1), content_type = "application/json")
		self.assertEqual(response.status_code,201)
		self.assertEqual(json.loads(response.get_data()),{
			    "USERS": [
        {
            "Name": "Simon Siva",
            "email": "sudi",
            "isAdmin": True,
            "password": "4fgrct745",
            "phoneNumber": "908374647",
            "registeredOn": today_now.strftime("%d/%m/%Y"),
            "u_id": 1,
            "userName": "simftgon"
        }
    ],
    "status": 201
		})

	def test_missing_value(self):
		response = self.client.post("/api/v1/users/", data = json.dumps(self.user2), content_type = "application/json")
		self.assertEqual(response.status_code,400)
		self.assertEqual(json.loads(response.get_data()),{
			    "message": "Please fill in all required details",
    				"status": 400	
		})
	def test_login(self):
		response = self.client.post("/api/v1/users/auth/", data = json.dumps(self.user3), content_type = "application/json")
		self.assertEqual(response.status_code, 200)
	
	def test_login_missing_email(self):
		response = self.client.post("/api/v1/users/auth/", data = json.dumps(self.user4), content_type = "application/json")
		self.assertEqual(response.status_code, 400)
	def test_login_missing_password(self):
		response = self.client.post("/api/v1/users/auth/", data = json.dumps(self.user5), content_type = "application/json")
		self.assertEqual(response.status_code, 400)
""" Users Models"""

import datetime, os
from datetime import date

USERS = [
]

class UserModel():
	def __init__(self, Name, registeredOn, email, userName, password, phoneNumber, isAdmin):

		registeredOn = datetime.datetime.now()
		registeredOn = registeredOn.strftime("%d/%m/%Y")
		self.registeredOn = registeredOn
		self.Name = Name
		self.email = email
		self.userName = userName
		self.password = password
		self.phoneNumber = phoneNumber
		self.isAdmin = isAdmin
		self.u_id = len(USERS) + 1
	
	def create_user(self):
		user = {
			"u_id":self.u_id,
			"registeredOn":self.registeredOn,
			"Name":self.Name,
			"email":self.email,
			"userName":self.userName,
			"phoneNumber":self.phoneNumber,
			"password":self.password,
			"isAdmin":self.isAdmin
		}
		USERS.append(user)
		return USERS

	@classmethod
	def login_user(cls, email, password):
		
		for user in USERS:
			if (user["email"] == email and user["password"] == password):
				userl = {"USER" : user["Name"],
				"password":user["password"],
				"email":user["email"],
				"userName":user["userName"],
				"isAdmin":user["isAdmin"],
				"phoneNumber":user["phoneNumber"]}
				
				return userl
				
		

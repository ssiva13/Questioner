""" This model hadles users """

from datetime import datetime, timedelta, date
import os, jwt
from instance.config import Config
from app.conn import init_db

USERS = []
SECRET_KEY = Config.JWT_SECRET_KEY
token = {}

class UserModels(object):
    """ A class that maps user data """
    
    def __init__(self):
        self.USR = init_db()
        self.users = USERS
    
    def generate_token(self, email):
        """ Generate auth token """
        try:
            payload = {'exp': date.today() + timedelta(days=0, minutes=30, seconds=0), 'iat': datetime.utcnow(), 'sub': email}
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        except Exception as e:
            return e

    def verify_token(self, auth_token):
        """Verify auth token """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token exppired, login again'
        except jwt.InvalidTokenError:
            return 'Invalid token, login'
    
    def signup(self, Name, email, phoneNumber, userName, isAdmin, password):
        """ Method to manipulate addition of new users into the database"""

        usere = {
            "Name": Name,
            "userName": userName,
            "email": email,
            "phoneNumber": phoneNumber,
            "isAdmin": isAdmin,
            "password": password
        }

        cursor = self.USR.cursor()
        cursor.execute(
            """SELECT email FROM users WHERE email = '%s'""" %(email))
        user = cursor.fetchone()
        
        #return  user
        
        if user:
            status_code = 409
            data = ["Email Already Exists", status_code]
            return  data
         
        else:
            query = """INSERT INTO users (Name, userName, email, phone, isAdmin, password, created_at) 
	   			VALUES ( %(Name)s, %(userName)s,%(email)s, %(phoneNumber)s,
                 %(isAdmin)s, %(password)s, CURRENT_TIMESTAMP ) RETURNING *"""
            cursor.execute(query,usere)
            user = cursor.fetchone()
            self.USR.commit()
            cursor.close()
            status_code = 201
            data = [user, status_code]

            return data
         

    def login(self, email):
        """ Get user by using email """
        cursor = self.USR.cursor()
        cursor.execute(
            """ SELECT email, password FROM users WHERE email = '%s' """ % (email)
        )
        user = cursor.fetchone()
        cursor.close()
        return user
import unittest, pytest, datetime, json, instance
from flask import current_app, Flask, request
from app.api.v1.views import question_views
from app.api.v1.models import questions_models
from app.api.v1.views.question_views import question_bp
from run import app
from datetime import date

class BaseTest(unittest.TestCase):
	
    def setUp(self):
	    self.app = app
	    self.client = self.app.test_client()

	    self.question1 = {
			"body" : "How do I prepare a rice nursery",
			"createdOn" : "",
			"createdBy" : "Simon Siva",
			"meetup" : 2,
			"q_id": 1,
			"title" : "Nursery",
			"votes" : 4
	   		}
	    self.question2 = {
			"createdOn" : "",
			"createdBy" : "",
			"meetup" :"" ,
			"title" : "Nursery",
			"votes" : 32,
			"body" : "How do I prepare a rice nursery"
	   		}
	
	
	   
    #def 
    
    
    #def

    def tearDown(self):
        pass

class TestQuestion(BaseTest):
	
	def test_created_meetup_success(self):
		#target_time = date.today() + datetime.timedelta(days=10)
		today_now = date.today()

		response = self.client.post('/api/v1/questions', data=json.dumps(self.question1), content_type="application/json")
		self.assertEqual(response.status_code,201)
		self.assertEqual(json.loads(response.get_data()),
{
    "QUESTIONS": [
        {
            "body": "How do I prepare a rice nursery",
            "createdBy": "Simon Siva",
            "createdOn": today_now.strftime("%d/%m/%Y"),
            "meetup": 2,
            "q_id": 1,
            "title": "Nursery",
            "votes": 4
        }
    ],
    "status": 201
}
		)

				    
	def test_created_meetup_fail(self):
		response = self.client.post('/api/v1/questions', data=json.dumps(self.question2), content_type="application/json")
		self.assertEqual(response.status_code, 400)
		self.assertEqual(json.loads(response.get_data()),
		{
    			"message": "Please fill in all the required fields",
    			"status": 400
				})
		
	def test_upvote_success(self):
		response = self.client.patch('/api/v1/questions/1/upvote/', data=json.dumps(self.question1), content_type= 'application/json')
		self.assertEqual(response.status_code, 202)
		self.assertEqual(json.loads(response.get_data()),{
			    "Question": {
        				"body": "How do I prepare a rice nursery",
        				"meetup": 2,
        				"old_vote_count": 4,
        				"q_id": 1,
        				"title": "Nursery",
        				"votes": 5
    					},
    						"status": 202
		    			})
			
	def test_upvote_fail(self):
		response = self.client.patch('/api/v1/questions/5/upvote/', data=json.dumps(self.question1), content_type= 'application/json')
		self.assertEqual(response.status_code, 404)
		self.assertEqual(json.loads(response.get_data()),{
			    "message": "The question record was not found",
    				"status": 404
				})

	def test_downvote_success(self):
		response = self.client.patch('/api/v1/questions/1/downvote/', data=json.dumps(self.question1), content_type= 'application/json')
		self.assertEqual(response.status_code, 202)
		self.assertEqual(json.loads(response.get_data()),{
			    "Question": {
        				"body": "How do I prepare a rice nursery",
        				"meetup": 2,
        				"old_vote_count": 4,
        				"q_id": 1,
        				"title": "Nursery",
        				"votes": 3
    					},
    						"status": 202
		    			})

	def test_downvote_fail(self):
		response = self.client.patch('/api/v1/questions/5/upvote/', data=json.dumps(self.question1), content_type= 'application/json')
		self.assertEqual(response.status_code, 404)
		self.assertEqual(json.loads(response.get_data()),{
			    "message": "The question record was not found",
    				"status": 404
				})
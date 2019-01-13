import unittest, pytest, datetime, json, instance
from flask import current_app, Flask, request
from app.api.v1.views import meetups_views
from app.api.v1.models import meetup_models
from app.api.v1.views.meetups_views import meetups_bp
from run import app
from datetime import date

class BaseTest(unittest.TestCase):
	
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

        #target_time = date.today() + datetime.timedelta(days=10)
        
        #today_now = date.today()

        self.meetup1 = {
            "topic": "My first meetup",
            "details":
		  "Lorem Lorem Ipsum has it all",
            "location": "Home",
            "happeningOn": "21/01/2019",
            "tags": "coding"
	 
		}

       

        self.meetup2 = {
		  "createdOn":"11/01/2019",
		  "topic": "",
            "details": "Lorem Lorem Ipsum has it all",
            "location": "Home",
            "happeningOn": "21/01/2019",
            "tags": "enjoy"
        }

    def tearDown(self):
        pass


class TestMeetup(BaseTest):
	
	def test_created_meetup_success(self):
		#target_time = date.today() + datetime.timedelta(days=10)
		today_now = date.today()

		response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup1), content_type="application/json")
		self.assertEqual(response.status_code,201)
		self.assertEqual(json.loads(response.get_data()),{
		    	"MEETUPS": [
        				{
            			"Tags": "coding",
            			"createdOn": today_now.strftime("%d/%m/%Y"),
            			"details": "Lorem Lorem Ipsum has it all",
            			"happeningOn": "21/01/2019",
            			"location": "Home",
            			"m_id": 1,
            			"topic": "My first meetup"
					  }
    				]})

				    
	def test_created_meetup_fail(self):
		response = self.client.post('/api/v1/meetups', data=json.dumps(self.meetup2), content_type="application/json")
		self.assertEqual(response.status_code, 400)
		self.assertEqual(json.loads(response.get_data()),
			{
			    "message": "Please fill in all the required details",
    				"status": 400
				    })
	
	def test_get_meetups_all_success(self):
		today_now = date.today()
		response = self.client.get('/api/v1/meetups/upcoming/', data=json.dumps(self.meetup2), content_type="application/json")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.get_data()),
		{
    		"MEET-UP": [{    	
			     "createdOn":today_now.strftime("%d/%m/%Y"),
				"details": "Lorem Lorem Ipsum has it all",
            		"happeningOn": "21/01/2019",
            		"location": "Home",
            		"Tags":"coding",
				"m_id":1,
            		"topic": "My first meetup"
        		}],
			   "status":200})
	def test_get_single_meetup(self):
		today_now = date.today()
		response = self.client.get('/api/v1/meetups/1', data=json.dumps(self.meetup2), content_type="application/json")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(json.loads(response.get_data()),
		{
    		"MEET UP": {
        		"Tags": "coding",
        		"createdOn": today_now.strftime("%d/%m/%Y"),
        		"details": "Lorem Lorem Ipsum has it all",
        		"happeningOn": "21/01/2019",
        		"location": "Home",
        		"m_id": 1,
        		"topic": "My first meetup"
    		},
    			"status": 200
		}
		)
	
	def test_get_single_meetup_id_not_found(self):
		response = self.client.get('/api/v1/meetups/19', data=json.dumps(self.meetup1), content_type="application/json")
		self.assertEqual(response.status_code, 404)
		

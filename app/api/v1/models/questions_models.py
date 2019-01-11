""" Models for handling Meetup data """
"""Meetup models"""

import datetime
""" Initialize list to hold all meetups"""
Questions = []


"""Class model for storing meetups data"""

class QuestionModel():
	"""Meetup instance variable"""
	def __init__(self,createdOn,createdBy, body, title,meetup,votes):

		createdOn=datetime.datetime.now()
		createdOn=createdOn.strftime("%d/%m/%Y")
		self.createdOn=createdOn
		self.createdBy=createdBy
		self.votes=votes
		self.title=title
		self.meetup=meetup
		self.body=body
		self.q_id=len(Questions)+1
	def post_question(self):
		question = {
			"q_id":self.q_id,
			"body":self.body,
			"createdOn":self.createdOn,
			"createdBy":self.createdBy,
			"title":self.title,
			"meetup":self.meetup,
			"votes":self.votes
			
		}
		Questions.append(question)
		return Questions
	
	
""" Models for handling Meetup data """
"""Meetup models"""

import datetime
""" Initialize list to hold all questions"""
Questions = []


"""Class model for storing questions data"""

class QuestionModel():
	"""Meetup instance variable"""
	def __init__(self,createdOn,createdBy, votes, title,meetup,body):

		createdOn=datetime.datetime.now()
		createdOn=createdOn.strftime("%d/%m/%Y %H:%M")
		self.createdOn=createdOn
		self.createdBy=createdBy
		self.title=title
		self.meetup=meetup
		self.body=body
		self.votes=votes
		self.q_id=len(Questions)+1
	def post_question(self):
		question = {
			"q_id":self.q_id,
			"createdOn":self.createdOn,
			"createdBy":self.createdBy,
			"title":self.title,
			"votes":self.votes,
			"meetup":self.meetup,
			
			"body":self.body
			
		}
		Questions.append(question)
		return Questions
	
	
""" Models for handling question data """
"""Meetup models"""

import datetime

""" Initialize list to hold all questions"""
Questions = []


"""Class model for storing meetups data"""

class QuestionModel():
	"""Meetup instance variable"""
	def __init__(self,createdBy, createdOn, body, title,meetup,votes):

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

	@classmethod
	def vote_question(cls, q_id):
		"""check if question id is greater than length of dict"""

		if q_id<=len(Questions):	
			que = Questions[q_id-1]
			que1 = {
				"q_id" 	: 	que["q_id"],
				"title"	:	que["title"],
				"meetup"	:	que["meetup"],
				"body"	:	que["body"],
				"votes"	:	que["votes"]
				}
			return que1
		return "The question record was not found"
  
	
	
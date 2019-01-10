"""Meetup models"""

import datetime
""" Initialize list to hold all meetups"""
Meetups = []


"""Class model for storing meetups data"""

class MeetupsModel():
	"""Meetup instance variable"""
	def __init__(self,topic,details,location,happeningOn,tags):
		self.topic=topic
		self.details=details
		self.location=location
		self.happeningOn=happeningOn
		self.tags=tags
		createdOn=datetime.datetime.now()
		createdOn=createdOn.strftime("%d/%m/%Y %H:%M")
		self.createdOn=createdOn
		'''self.images=images'''
		self.m_id=len(Meetups)+1
	def create_meetup(self):
		meetup = {
			"m_id":self.m_id,
			"topic":self.topic,
			"details":self.details,
			"createdOn":self.createdOn,
			"location":self.location,
			"happeningOn":self.happeningOn,
			
			"Tags":self.tags
			
		}
		Meetups.append(meetup)
		return Meetups
	@classmethod
	def get_meetup(cls, m_id):
		"""check if meetup id is greater than length of dict"""
		if m_id > len(Meetups):
			return "The meetup record was not found"
		meetup = Meetups[m_id-1]
		meetup1 = {"id" : meetup["m_id"],"topic":meetup["topic"],"details":meetup["details"],"createdOn":meetup["createdOn"],"location":meetup["location"],
		"happeningOn":meetup["happeningOn"],"Tags":meetup["Tags"] }
		return meetup1

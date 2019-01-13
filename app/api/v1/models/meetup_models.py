"""Meetup models"""

import datetime

from datetime import date

""" Initialize list to hold all meetups"""
Meetups = [  ]
RSVPS =[]


"""Class model for storing meetups data"""

class MeetupsModel():
	"""Meetup instance variable"""
	def __init__(self,topic,details,location,happeningOn,tags):
		self.topic=topic
		self.details=details
		self.location=location

		self.tags=tags
		createdOn=date.today()
		createdOn=createdOn.strftime("%d/%m/%Y")
		#happeningOn=date.today() + datetime.timedelta(days=7)
		self.happeningOn=happeningOn

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

		if m_id>len(Meetups):
			return "The meetup record was not found"
		meetup = Meetups[m_id-1]
		meetup1 = {"m_id" : meetup["m_id"],"topic":meetup["topic"],"details":meetup["details"],"createdOn":meetup["createdOn"],"location":meetup["location"],

		"happeningOn":meetup["happeningOn"],"Tags":meetup["Tags"] }
		return meetup1

	@classmethod
	def get_upcoming(cls):
		"""check if there are any meetups"""
		if len(Meetups) == 0:
			return "No meetups"
		
		return Meetups

class MeetUpRsvps():

	@classmethod
	def add_rsvps(cls, m_id):
		if m_id<len(Meetups):
			m_ide = Meetups[m_id-1]
			meetup1 = {"m_id" : m_ide["m_id"],
				"topic":m_ide["topic"]
				}
			return meetup1
		return "The meetup record was not found"
				

	
		

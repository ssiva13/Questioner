""" This model handles users """

from datetime import datetime, timedelta, date

from app.conn import init_db

MEETUPS = []
RSVPS = []

class MeetupModels(object):
    """ A class that maps user data """
 
    def __init__(self):
        self.MTP = init_db()
        self.meetups = MEETUPS

    def createmeetup(self, topic, details, location, happeningOn, image):
        """ Method to manipulate addition of new users into the database"""

        meetup = {
            "topic": topic,
            "details": details,
            "location": location,
            "happeningOn": happeningOn,
            "image": image
        }

        cursor = self.MTP.cursor()
        
        query = """INSERT INTO meetups (topic, details, location, happeningOn, image, createdOn) 
	   			VALUES ( %(topic)s, %(details)s, %(location)s, %(happeningOn)s,
	   			%(image)s, CURRENT_TIMESTAMP ) RETURNING *"""

        cursor.execute(query,meetup)
        meetupd = cursor.fetchone()
        self.MTP.commit()
        cursor.close()

        return meetupd

    def get_meetup(self, m_id):
        """ Get meetup by using meetup id """
        cursor = self.MTP.cursor()
        cursor.execute(
            """ SELECT * FROM meetups WHERE m_id = '%d' """ % (m_id)
        )
        meetup = cursor.fetchone()
        cursor.close()
        return meetup

    def get_upcoming(self):
        """ Get meetups """
        cursor = self.MTP.cursor()
        cursor.execute(""" SELECT * FROM meetups """)
        meetup = cursor.fetchall()
        cursor.close()
        return meetup
         
    def delete_meetup(self, m_id):
	    """ Get meetup by using meetup id """
	    cursor = self.MTP.cursor()
	    cursor.execute(
            """ DELETE FROM meetups WHERE m_id = '%d' """ % (m_id)	)   

	    self.MTP.commit()
	    
	    cursor = self.MTP.cursor()
	    cursor.execute(""" SELECT * FROM meetups """)

	    meetup = cursor.fetchall()
	    cursor.close()
	    return meetup
    #def rsvp_meetup(self, m_id):
	    

"""HAndles Views meetup endpoints"""
from flask import Blueprint, jsonify, request, make_response, json
from ..models.meetup_models import MeetupModels
#from ..models.meetup_models import MeetUpRsvps
from ..models.meetup_models import MEETUPS
from ..models.meetup_models import RSVPS


"""Create Blueprint for meetups"""
meetups_v2 = Blueprint("meetupsv2",__name__, url_prefix='/api/v2/')


@meetups_v2.route("/")
def home():
	return 'Farming test Verion 2'

@meetups_v2.route("/meetups", methods=["POST"])
def create_meetup():
	""" A view to control creation of users """
	try:
		data = request.get_json()
	except:
		return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400
	topic = data.get("topic")
	details = data.get("details")
	location = data.get("location")
	happeningOn = data.get("happeningOn")
	image = data.get("image")

	if not topic:
		return make_response(jsonify({
            "status": 400,
            "message": "Topic is required"
        })), 400
	if not details:
		return make_response(jsonify({
            "status": 400,
            "message": "Details are required"
        })), 400
	if not location:
		return make_response(jsonify({
            "status": 400,
            "message": "Location is required"
        })), 400
	if not happeningOn:
		return make_response(jsonify({
            "status": 400,
            "message": "Date is required"
        })), 400
	meet = MeetupModels()
	meetup =meet.createmeetup(topic, details, location, happeningOn, image )
	return make_response(jsonify({"status": 201,"MEETUP": meetup} )), 201

@meetups_v2.route('/meetups/<int:m_id>', methods=['GET'])
def get_meetup(m_id):
	meet = MeetupModels()
	meetup= meet.get_meetup(m_id)

	if meetup:
		return make_response(jsonify({
                "status": 200,
                "MEETUP": meetup
            })), 200
	return make_response(jsonify({
        "status": 404,
        "message": "Meetup does not exist."
    })), 404


@meetups_v2.route('/meetups/upcoming/', methods=['GET'])
def get_upcoming():
	meet = MeetupModels()
	meetup= meet.get_upcoming()

	if meetup:
		return make_response(jsonify({
                "status": 200,
                "MEETUPS": meetup
            })), 200
	return make_response(jsonify({
        "status": 404,
        "message": "No meetups found"
    })), 404


@meetups_v2.route('/meetups/<int:m_id>', methods=['delete'])
def delete_meetup(m_id):

	meet = MeetupModels()
	meetup= meet.delete_meetup(m_id)

	if meetup:
		return make_response(jsonify({
                "status": 200,
                "MEETUPS": meetup
            })), 200
	return make_response(jsonify({
        "status": 404,
        "message": "Meetup does not exist."
    })), 404
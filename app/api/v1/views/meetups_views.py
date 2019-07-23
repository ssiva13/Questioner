"""HAndles Views meetup endpoints"""
from flask import Blueprint, jsonify, request, make_response, json,  render_template
from ..models.meetup_models import MeetupsModel
from ..models.meetup_models import MeetUpRsvps
from ..models.meetup_models import Meetups
from ..models.meetup_models import RSVPS




"""Create Blueprint for meetups"""
meetups_bp = Blueprint("meetups",__name__, url_prefix='/api/v1/')



@meetups_bp.route("/")
def home():
	urls = 'https://questioner13.herokuapp.com/api/v1/'
	return render_template('index.html', urls = urls)


"""Endpoint to create A meetup"""
@meetups_bp.route("/meetups", methods=["POST"])
def create_meetup():

	topic = request.json["topic"]
	details = request.json["details"]
	location = request.json["location"]
	happeningOn = request.json["happeningOn"]
	Tags = request.json["Tags"]

	"""Checking json values"""
	if not topic or not details or not location or not happeningOn or not Tags:
		return jsonify({
			"status":400,
			"message":"Please fill in all the required details"}), 400

	"""""If all required fields are filled proceed"""""
	meetup = MeetupsModel(topic, details, location, happeningOn, Tags)
	data_submitted = meetup.create_meetup()
	return make_response(jsonify({
			"status": 201,
			"MEETUPS":data_submitted
			})),201



@meetups_bp.route("/meetups/<int:m_id>", methods=["GET"])
def get_meetup(m_id):

	meetup = MeetupsModel.get_meetup(m_id)
	""" If it exists"""
	if type(meetup)==dict:
		return jsonify({
			"status":200,
			"MEET UP" : meetup}), 200
	return jsonify({
		"status":404,
		"message" : meetup}), 404



@meetups_bp.route("/meetups/upcoming/", methods=["GET"])
def get_mp_upcoming():
	meetups_up = MeetupsModel.get_upcoming()
	""" If any exists"""
	if type(meetups_up)==list:
		return jsonify({
			"status":200,
			"MEET-UP" : meetups_up}), 200
	return jsonify({
		"status":404,
		"message" : "Meetup was not found"}), 404

@meetups_bp.route("/meetups/<int:m_id>/rsvps/", methods=["POST"])
def rsvps_meetup(m_id):
	u_id = request.json["u_id"]
	resp = request.json["resp"]
	#meetup = ""

	"""Checking ids and response"""
	
	if not resp or not u_id or not m_id:
		return make_response(jsonify({
			"status":400,
			"message":"Please give a valid rsvp feedback"
		})), 400
	
	rsvp4 = MeetUpRsvps.add_rsvps(m_id)
	data ={"resp":resp,"u_id":u_id}
	if type(rsvp4)==dict:
		rsvp4.update(data)
		RSVPS.append(rsvp4)

		return make_response(jsonify({
			"status": 201,
			"My RSVPed MEETUPS": RSVPS
		})), 201
	#RSVPS.append(rsvp4)
	return make_response(jsonify({
		"status":404,
		"message":rsvp4
	})),404

@meetups_bp.route("/meetups/<int:m_id>/delete/", methods=["delete"])
def delete_meetup(m_id):

	meetupd = MeetupsModel.get_meetup(m_id)
	""" If it exists"""
	if type(meetupd)==dict:
		Meetups.remove(meetupd)
		return jsonify({
			"status":200,
		"message" : "The selected meetup was deleted successfully",
		"MEETUPS":Meetups
			}), 200
	return jsonify({
		"status":404,
		"MESSAGE" : meetupd,
		#"MEETUPS": Meetups
			}), 404

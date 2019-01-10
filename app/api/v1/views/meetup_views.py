"""HAndles Views meetup endpoints"""
from flask import Blueprint, jsonify, request
from ..models.meetup_models import MeetupsModel



"""Create Blueprint for meetups"""
meetups_bp = Blueprint("meetups",__name__, url_prefix='/api/v1/')



@meetups_bp.route("/")
def home():
	return 'Farming test'


"""Endpoint to create A meetup"""
@meetups_bp.route("/meetups", methods=["POST"])
def create_meetup():
	topic = request.json["topic"]
	details = request.json["details"]
	location = request.json["location"]
	happeningOn = request.json["happeningOn"]
	tags = request.json["tags"]

	"""Checking json values"""
	if not topic or not details or not location or not happeningOn or not tags:
		return jsonify({
			"status":400,
			"message":"Please fill in all the required details"}), 400

	"""""If all required fields are filled proceed"""""
	meetup = MeetupsModel(topic, details, location, happeningOn, tags)
	data_submitted = meetup.create_meetup()
	return jsonify({
		"status":201,
		"MEETUPS":data_submitted}),201


@meetups_bp.route("/meetups/<int:m_id>", methods=["GET"])
def get_meetup(m_id):
	meetup = MeetupsModel.get_meetup(m_id)
	""" If it exists"""
	if type(meetup)==dict:
		return jsonify({
			
			"MEET UP" : meetup}), 200
	return jsonify({
		"status":404,
		"message" : "Meetup was not found"}), 404


'''
@meetups_bp.route("/meetups/upcoming/", methods=["GET"])
def get_upcoming_meetup(happeningOn):
	meetups = MeetupsModel.get_upcoming_meetup(happeningOn)
	""" If any exists"""
	if type(meetups)==dict:
		return jsonify({"MEET UP" : meetups}), 200
	return jsonify({
		"status":404,
		"message" : "Meetup was not found"}), 404
'''
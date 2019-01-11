""" Views for handling question endpoints """

from flask import Flask, Blueprint, request, make_response, jsonify
from ..models.questions_models import QuestionModel
from werkzeug.exceptions import BadRequest

question_bp = Blueprint('questions', __name__, url_prefix='/api/v1/')


@question_bp.route("/ha")
def home():
	return 'Farmrtrtyring test'


"""Endpoint to create A meetup"""
@question_bp.route("/questions", methods=["POST"])
def create_meetup():
	createdOn = request.json["createdOn"]
	createdBy = request.json["createdBy"]
	body = request.json["meetup"]
	title = request.json["title"]
	meetup = request.json["body"]
	votes = request.json["votes"]
	

	"""Checking json values"""
	if  not createdBy or not meetup or not title or not votes or not body:
		return jsonify({
			"status":400,
			"message":"Please fill in all the required fields"}), 400

	"""""If all required fields are filled proceed"""""
	question = QuestionModel(createdBy, createdOn, meetup, title, body, votes)
	data_submitted = question.post_question()
	return jsonify({
		"status":201,
		"QUESTIONS":data_submitted}),201

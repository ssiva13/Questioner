""" Views for handling question endpoints """

from flask import Flask, Blueprint, request, make_response, jsonify
from ..models.questions_models import QuestionModel
from werkzeug.exceptions import BadRequest

question_bp = Blueprint('questions', __name__, url_prefix='/api/v1/')


@question_bp.route("/ha")
def home():
	return 'Farmers Gala Test'


"""Endpoint to create A question"""
@question_bp.route("/questions", methods=["POST"])
def create_meetup():
	createdOn = request.json["createdOn"]
	createdBy = request.json["createdBy"]
	body = request.json["body"]
	title = request.json["title"]
	meetup = request.json["meetup"]
	votes = request.json["votes"]
	

	"""Checking json values"""
	if  not createdBy or not meetup or not title or not votes or not body:
		return jsonify({
			"status":400,
			"message":"Please fill in all the required fields"}), 400

	"""""If all required fields are filled proceed"""""
	question = QuestionModel(createdBy, createdOn, body, title, meetup, votes)
	data_submitted = question.post_question()
	return jsonify({
		"status":201,
		"QUESTIONS":data_submitted}),201

@question_bp.route('/questions/<int:q_id>/upvote/', methods=['PATCH'])
def upvote_que(q_id):
	que = QuestionModel.vote_question(q_id)
	if type(que)==dict:
		que1 ={
				"votes" : que["votes"] + 1,
				"old_vote_count": que["votes"],
				"q_id" 	: 	que["q_id"],
				"title"	:	que["title"],
				"meetup"	:	que["meetup"],
				"body"	:	que["body"],
			}
		#que1.update(que)
		return make_response(jsonify({
			"status": 202,
			"Question" : que1
		})), 202
	return make_response(jsonify({
				"status":404,
				"message":que
					})),404

@question_bp.route('/questions/<int:q_id>/downvote/', methods=['PATCH'])
def downvote_que(q_id):
	que = QuestionModel.vote_question(q_id)
	if que:
		que1 ={
				"votes" : que["votes"] - 1,
				"old_vote_count": que["votes"],
				"q_id" 	: 	que["q_id"],
				"title"	:	que["title"],
				"meetup"	:	que["meetup"],
				"body"	:	que["body"],
			}
		#que1.update(que)
		return make_response(jsonify({
			"status": 202,
			"Question" : que1
		})), 202

	return make_response(jsonify({
				"status":404,
				"message":que
					})),404
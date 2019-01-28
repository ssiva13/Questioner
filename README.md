[![Build Status](https://travis-ci.com/ssiva13/Questioner.svg?branch=develop)](https://travis-ci.com/ssiva13/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/ssiva13/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/ssiva13/Questioner?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a8e5683d035c482cae8ab493b585d80b)](https://www.codacy.com/app/ssiva13/Questioner?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ssiva13/Questioner&amp;utm_campaign=Badge_Grade)
[![Maintainability-Code CLimate](https://api.codeclimate.com/v1/badges/2e56adfb9a1f7c96da59/maintainability)](https://codeclimate.com/github/ssiva13/Questioner/maintainability)



# Questioner-api
It is a crowd-sourcing platform for meetup questions. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

## Prerequisites
- Python 3.6.7 
- Postman
- PostgreSQL

## Installation
1. Clone this repository :

	```
    $ git clone https://github.com/ssiva13/Questioner.git
    ```

2. CD into the project folder on your machine

	```
    $ cd Questioner
    ```

3. Create a virtual environment

    ```
    $ python3 -m venv venv
    ```

4. Activate the virtual environment

	```
    $ source venv/bin/activate
    ```

5. Install the dependencies from the requirements file

	```
    $ pip3 install -r requirements.txt
    ```

6. Run the application

    ```
    flask run
    ```

## Testing API endpoint

|------------------------------------------------------------------------------------------------------------------------|
|											  Version 1											 |
| ---------------------------------------------------- | ----------- | --------------------------------------------------|
| Endpoint                            				| HTTP Verb   | Functionality           			    		 |
| ---------------------------------------------------- | ----------- | --------------------------------------------------|
| /api/v1/meetups                  				| POST        | Create a meetup record     			    		 |
| /api/v1/meetups/<meetup_id>          				| GET         | Fetch a specific meetup record   		    		 |
| /api/v1/meeetups/upcoming/          		 		| GET         | Fetch all upcoming meetup records          		 |
| /api/v1/questions                				| POST        | Create a question for a specific meetup    		 |
| /api/v1/questions/<question_id>/upvote			| PATCH       | Up-vote a specific question        	    		 |
| /api/v1/questions/<question_id>/downvote			| PATCH       | Down-vote a specific question       	    		 |
| /api/v1/meetups/<meetup_id>/rsvps   				| POST        | RSVP a specific meetup    					 |
| /api/v1/auth/signup   							| POST        | Endpoint for user account creation    			 |
| /api/v1/auth/login   							| POST        | Endpoint for user login    					 |
| /api/v1/comments/   							| POST        | Post comments to a question for a specific meetup |
| /api/v1/meetups/<meetup_id>/   					| DELETE      | Delete a specific meetup    					 |
| /api/v1/meetups/<meetup_id>/images   				| POST        | Add image resource to a specific meetup    		 |
--------------------------------------------------------------------------------------------------------------------------

|------------------------------------------------------------------------------------------------------------------------|
|											   Version 2											 |
| ---------------------------------------------------- | ----------- | --------------------------------------------------|
| Endpoint                            				| HTTP Verb   | Functionality           			    		 |
| ---------------------------------------------------- | ----------- | --------------------------------------------------|
| /api/v2/meetups                  				| POST        | Create a meetup record     			    		 |
| /api/v2/meetups/<meetup_id>          				| GET         | Fetch a specific meetup record   		    		 |
| /api/v2/meeetups/upcoming/          		 		| GET         | Fetch all upcoming meetup records          		 |
| /api/v2/questions                				| POST        | Create a question for a specific meetup    		 |
| /api/v2/questions/<question_id>/upvote			| PATCH       | Up-vote a specific question        	  	  	 |
| /api/v2/questions/<question_id>/downvote			| PATCH       | Down-vote a specific question       	    		 |
| /api/v2/meetups/<meetup_id>/rsvps   				| POST        | RSVP a specific meetup    					 |
| /api/v2/auth/signup   							| POST        | Endpoint for user account creation    			 |
| /api/v2/auth/login   							| POST        | Endpoint for user login    					 |
| /api/v2/comments/   							| POST        | Post comments to a question for a specific meetup |
| /api/v2/meetups/<meetup_id>/   					| DELETE      | Delete a specific meetup    					 |
| /api/v2/meetups/<meetup_id>/images   				| POST        | Add image resource to a specific meetup    		 |
--------------------------------------------------------------------------------------------------------------------------


## Authors
Simon Siva - [Simon Siva](https://github.com/ssiva13)

## License


## Acknowledgement
-Andela Workshops
-Team 1 members
-NBO36


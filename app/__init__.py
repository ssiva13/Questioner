from flask import Flask
from instance.config import app_config
from .api.v1.views.meetups_views import meetups_bp
from .api.v1.views.question_views import question_bp

def create_app(config_name):

    """ Using the config file in instance folder to create app """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config)
    
    ##app.register_blueprint(meetups_bp)
    ##app.register_blueprint(question_bp)
    
    
    return app
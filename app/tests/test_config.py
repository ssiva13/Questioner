import unittest
from flask import current_app, Flask
import instance

app = Flask(__name__, instance_relative_config=True)

class TestConfig(unittest.TestCase):
	def test_config(self):
		app.config.from_object(instance.config.Config)
		self.assertTrue(app.config['DEBUG'] is False)

class TestDevelopmentConfig(unittest.TestCase):
    def test_development(self):
        app.config.from_object(instance.config.Development)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

class TestTestingConfig(unittest.TestCase):
    def test_testing(self):
        app.config.from_object(instance.config.Testing)
        self.assertTrue(app.config['DEBUG'])

class TestProductionConfig(unittest.TestCase):
    def test_production(self):
        app.config.from_object(instance.config.Production)
        self.assertTrue(app.config['DEBUG'] is False)

if __name__ == '__main__':
	unittest.main()
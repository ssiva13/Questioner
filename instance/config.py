import os

class Config(object):
    """ Main configurations class """
    DEBUG = False
    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret')
    DATABASE_URL = os.getenv('DB_URL')
    DATABASE_TEST_URL = os.getenv('DB_TEST_URL')

class Development(Config):
    """ Development configurations are put here """
    DEBUG = True

class Testing(Config):
    """ The configurations for testing """
    DEBUG = True
    TESTING = True

class Production(Config):
    """ The production configurations """
    DEBUG = False
    TESTING = False

app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
}
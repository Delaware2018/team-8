import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = "postgres://ycfwfrua:u1u7FGchZENVMu6smfV5dW_B67c_35sM@elmer.db.elephantsql.com:5432/ycfwfrua"

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

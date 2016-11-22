import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
SECRET_KEY = 'uhrmaHghurds3craTC0de!'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'postgres://ipybegwihbxqsq:5DPp9C7Ge8epW-X5OfbyQAC6U4@ec2-54-235-65-221.compute-1.amazonaws.com:5432/d13as5liieseeo'
MAIL_DEFAULT_SENDER = "matthew@opendata.durban"

# Flask-Security config
SECURITY_URL_PREFIX = "/user"
SECURITY_PASSWORD_HASH = "sha256_crypt"
SECURITY_PASSWORD_SALT = "sha256_crypt"
# SECURITY_USER_IDENTITY_ATTRIBUTES = 'name'

# Flask-Security admin
SECURITY_EMAIL_SENDER = MAIL_DEFAULT_SENDER

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_CHANGE_URL = "/change-password/"
SECURITY_RESET_URL = "/forgot-password"

# Flask-Security email subject lines
SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to HealthTools-EC"
SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = "Password reset instructions for your HealthTools-EC account"

# Flask-Security features
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
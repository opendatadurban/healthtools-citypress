import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_ENABLED = True
SECRET_KEY = 'uhrmaHghurds3craTC0de!'
SQLALCHEMY_DATABASE_URI = 'postgresql://gibela_dev:gibela_dev@localhost/gibela_dev'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

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
SECURITY_EMAIL_SUBJECT_REGISTER = "Welcome to Gibela"
SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = "Password reset instructions for your Gibela account"

# Flask-Security features
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
import os
from flask import Flask

app = Flask(__name__, static_folder='static')
env = 'production'
app.config['ENV'] = env
app.config.from_pyfile('config_prod.py')

from flask_mako import MakoTemplates, _lookup, render_template
import haml

MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = haml.preprocessor
app.config['MAKO_TRANSLATE_EXCEPTIONS'] = False
app.config['MAKO_DEFAULT_FILTERS'] = ['decode.utf8']
# app.config['SECURITY_USER_IDENTITY_ATTRIBUTES'] = ('name', 'email')

# CSRF protection
from flask_wtf.csrf import CsrfProtect

CsrfProtect(app)

# Database
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# Mail
from flask_mail import Mail

mail = Mail(app)

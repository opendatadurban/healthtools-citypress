import os
from flask import Flask

app = Flask(__name__, static_folder='public')
env = os.environ.get('FLASK_ENV', 'development')
print env
raw_input('...')
app.config['ENV'] = env
app.config.from_pyfile('config.py')

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

db = SQLAlchemy(app)

# Mail
from flask_mail import Mail

mail = Mail(app)

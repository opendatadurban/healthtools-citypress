from gibela.app import app
from flask import url_for, redirect
from flask_mako import render_template
from flask_security import current_user

from gibela.models import db, User, Rider, Provider

import gibela.rider
import gibela.provider


@app.route('/')
def home():
    if current_user.is_authenticated:
        if current_user.has_role('provider'):
            return redirect(url_for('provider_dashboard'))

        if current_user.has_role('rider'):
            return redirect(url_for('rider_dashboard'))

        return render_template('noperms.haml')
    else:
        return redirect(url_for('security.login'))

from healthtools_ec.app import app
from flask import url_for, redirect, session
from flask_mako import render_template
from flask_security import current_user
from healthtools_ec.models import db, User

import healthtools_ec.surgeons
import healthtools_ec.reportsurgeons
import healthtools_ec.initiates


@app.route('/')
def home(lang=0):
    session['lang'] = lang
    if session['lang']:
        return render_template('home/index_x.haml')
    else:
        return render_template('home/home.haml')


@app.route('/admin')
def admin():
    if current_user.is_authenticated:
        if current_user.has_role('admin'):
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('noperms.haml')
    else:
        return redirect(url_for('security.login'))

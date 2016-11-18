from healthtools_ec.app import app
from flask import url_for, redirect, session, render_template
# from flask_mako import render_template
from flask_security import current_user
from healthtools_ec.models import db, User

import healthtools_ec.surgeons
import healthtools_ec.reportsurgeons
import healthtools_ec.initiates


@app.route('/')
def home():
    if 'lang' in session.keys():
        if session['lang']:
            return redirect(url_for('home_xh'))
        else:
            return redirect(url_for('home_en'))
    return redirect(url_for('home_xh'))


@app.route('/xh')
def home_xh():
    session['lang'] = 1
    return render_template('home/home_xh.html')


@app.route('/en')
def home_en():
    session['lang'] = 0
    return render_template('home/home.html')


@app.route('/about')
def about():
    if session['lang']:
        return render_template('about_xh.html')
    else:
        return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/find')
def widgets():
    if session['lang']:
        return render_template('widgets/searchsurgeon_xh.html')
    else:
        return render_template('widgets/searchsurgeon.html')
# @app.route('/admin')
# def admin():
#     if current_user.is_authenticated:
#         if current_user.has_role('admin'):
#             return redirect(url_for('admin_dashboard'))
#         else:
#             return render_template('noperms.haml')
#     else:
#         return redirect(url_for('security.login'))

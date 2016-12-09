from healthtools_ec.app import app
from flask import url_for, redirect, session, render_template
# from flask_mako import render_template
from flask_security import current_user
from healthtools_ec.models import db, User

import healthtools_ec.surgeons
import healthtools_ec.reportsurgeons
import healthtools_ec.initiates
import healthtools_ec.locate


@app.route('/')
def home():
    if 'lang' in session.keys():
        if session['lang']:
            return redirect(url_for('home_xh'))
        else:
            return redirect(url_for('home_en'))
    session['lang'] = 1
    return redirect(url_for('home_xh'))


@app.route('/xh')
def home_xh():
    session['lang'] = 1
    return render_template('templates/home/home_xh.html')


@app.route('/en')
def home_en():
    session['lang'] = 0
    return render_template('templates/home/home.html')


@app.route('/about')
def about():
    if 'lang' not in session.keys():
        redirect(url_for('home_xh'))
    if session['lang']:
        return render_template('templates/about/about_xh.html')
    else:
        return render_template('templates/about/about.html')


@app.route('/contact')
def contact():
    if 'lang' not in session.keys():
        redirect(url_for('home_xh'))
    if session['lang']:
        return render_template('templates/contact/contact_xh.html')
    else:
        return render_template('templates/contact/contact.html')



@app.route('/find')
def widgets():
    if 'lang' not in session.keys():
        redirect(url_for('home_xh'))
    if session['lang']:
        return render_template('templates/widgets/widget_searchsurgeon_xh.html')
    else:
        return render_template('templates/widgets/widget_searchsurgeon.html')


# @app.route('/admin')
# def admin():
#     if current_user.is_authenticated:
#         if current_user.has_role('admin'):
#             return redirect(url_for('admin_dashboard'))
#         else:
#             return render_template('noperms.haml')
#     else:
#         return redirect(url_for('security.login'))

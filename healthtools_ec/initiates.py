from healthtools_ec.app import app
from flask_mako import render_template
from flask import request, url_for, redirect, flash, make_response, session

from .models import db
from .models import *
from .models.initiates import InitiateForm


@app.route('/initiates', methods=['GET', 'POST'])
def initiates_home():
    form = InitiateForm()
    status = 200
    if request.method == 'POST':
        if form.validate():
            initiate = Initiate()
            with db.session.no_autoflush:
                form.populate_obj(initiate)
            db.session.add(initiate)
            db.session.commit()
            if session['lang']:
                flash('Thank you for submitting!')
            else:
                flash('Thank you for submitting!')
            return redirect(url_for('home'))
        else:
            if request.is_xhr:
                status = 412
            else:
                if session['lang']:
                    flash('Please correct the problems below and try again.', 'warning')
                else:
                    flash('Please correct the problems below and try again.', 'warning')

    if not request.is_xhr:
        if session['lang']:
            resp = make_response(render_template('initiates/initiates_x.haml', form=form))
        else:
            resp = make_response(render_template('initiates/initiates.haml', form=form))

    else:
        resp = ''

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})


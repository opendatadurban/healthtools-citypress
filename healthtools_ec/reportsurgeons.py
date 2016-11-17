from healthtools_ec.app import app
from flask_mako import render_template
from flask import request, url_for, redirect, flash, make_response

from .models import db
from .models import *
from .models.reportsurgeons import ReportForm


@app.route('/reportsurgeon', methods=['GET', 'POST'])
def reports_home():
    form = ReportForm()
    status = 200
    if request.method == 'POST':
        if form.validate():
            report = ReportSurgeon()
            with db.session.no_autoflush:
                form.populate_obj(report)
            db.session.add(report)
            db.session.commit()
            flash('Thank you for submitting!')
            return redirect(url_for('home'))
        else:
            if request.is_xhr:
                status = 412
            else:
                flash('Please correct the problems below and try again.', 'warning')

    if not request.is_xhr:

        resp = make_response(render_template('reportsurgeons/reportsurgeons.haml', form=form))

    else:
        resp = ''

    return (resp, status,
            # ensure the browser refreshes the page when Back is pressed
            {'Cache-Control': 'no-cache, no-store, must-revalidate'})

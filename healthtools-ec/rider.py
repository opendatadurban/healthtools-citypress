from healthtools-ec.app import app
from flask_mako import render_template
from flask_security import roles_accepted, current_user, login_required
from sqlalchemy.orm import joinedload

from .models import db, Rider, Provider
from .models.initiates import RequestForm


@app.route('/rider')
@login_required
@roles_accepted('rider')
def rider_dashboard():
    form = RequestForm()

    return render_template('rider/rider_dashboard.haml',
                           form=form)

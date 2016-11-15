from healthtools-ec.app import app
from flask_mako import render_template
from flask_security import roles_accepted, current_user, login_required
from sqlalchemy.orm import joinedload

from gibela.models import *


@app.route('/provider')
@login_required
@roles_accepted('monitor')
def provider_dashboard():
    # latest_docs = [x.id for x in Document.query.order_by(Document.created_at.desc()).limit(30)]
    #
    # latest_docs = Document.query\
    #     .options(
    #         joinedload('created_by'),
    #         joinedload('sources'),
    #         joinedload('topic'),
    #         joinedload('medium'),
    #     )\
    #     .filter(Document.id.in_(latest_docs))\
    #     .order_by(Document.created_at.desc())
    #
    # doc_groups = []
    # for date, group in groupby(latest_docs, lambda d: d.created_at.date()):
    #     doc_groups.append([date, list(group)])

    return render_template('dashboard/dashboard.haml',
                           doc_groups=doc_groups)

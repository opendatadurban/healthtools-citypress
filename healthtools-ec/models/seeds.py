from . import *  # noqa
from ..app import app


def seed_db(db):
    """ Add seed entities to the database. """
    with app.app_context():
        for x in User.create_defaults():
            db.session.add(x)

        # db.session.flush()

        # for x in Role.create_defaults():
        #     db.session.add(x)
        #
        # for x in Rider.create_defaults():
        #     db.session.add(x)
        #
        # for x in Provider.create_defaults():
        #     db.session.add(x)

        db.session.commit()

from healthtools-ec.models import db
from healthtools-ec.models.seeds import seed_db

db.drop_all()
db.create_all()
seed_db(db)

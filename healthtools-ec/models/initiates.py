from sqlalchemy.dialects.postgresql import JSON
from ..app import db
from ..forms import Form
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField, validators
from wtforms_components import TimeField , PhoneNumberField
from wtforms.validators import DataRequired, Length
from sqlalchemy_utils import PhoneNumber

class Initiate(db.Model):
    __tablename__ = 'initiates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone_number = db.Column(db.Unicode(20), unique=True)
    country_code = db.Column(db.Unicode(8), unique=True)
    initiate_problem = db.Column(db.String(255))
    date_record = db.Column(db.Date)
    time_record = db.Column(db.Time)

    phonenumber = db.orm.composite(
        PhoneNumber,
        phone_number,
        country_code
    )
    def __repr__(self):
        return '<id {}>'.format(self.id)


class InitiateForm(Form):
    name = StringField('Initiate Name', [validators.Length(min=1, max=25)], validators=[DataRequired()])
    phone_number = PhoneNumberField(
        country_code='ZA'
        display_format='international'
    )

    initiate_problem = StringField('Initiate Problem Description', [validators.Length(min=1, max=25)], validators=[DataRequired()])

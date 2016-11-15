from sqlalchemy.dialects.postgresql import JSON
from ..app import db
from ..forms import Form
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField, validators
from wtforms_components import TimeField , PhoneNumberField
from wtforms.validators import DataRequired, Length
from sqlalchemy_utils import PhoneNumber
from healthtools-ec.app import db
from sqlalchemy_utils import PhoneNumber

class Surgeon(db.Model):
    __tablename__ = 'surgeons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    id_number = db.Column(db.String(50), nullable= True)
    area = db.Column(db.String(255))
    phone_number = db.Column(db.Unicode(20), unique= True)
    country_code = db.Column(db.Unicode(8), unique= True)
    standard = db.Column(db.String(10), nullable= True)
    Category = db.Column(db.String(10), nullable= True)

    phonenumber = db.orm.composite(
        PhoneNumber,
        phone_number,
        country_code
    )

    def __repr__(self):
        return '<id {}>'.format(self.id)

class RegisterForm(Form):
    name = StringField('Initiate Name', [validators.Length(min=1, max=25)], validators=[DataRequired()])
    phone_number = PhoneNumberField(
        country_code='ZA'
        display_format='international'
    )

    area = StringField('Area where you work in', [validators.Length(min=1, max=25)], validators=[DataRequired()])


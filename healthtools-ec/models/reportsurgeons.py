from sqlalchemy.dialects.postgresql import JSON
from ..app import db
from ..forms import Form
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField, validators
from wtforms_components import TimeField , PhoneNumberField
from wtforms.validators import DataRequired, Length
from sqlalchemy_utils import PhoneNumber
from healthtools-ec.app import db
from sqlalchemy_utils import PhoneNumber

class Reportsurgeon(db.Model):
    __tablename__ = 'reportsurgeons'

    id = db.Column(db.Integer, primary_key=True)
    opt_name = db.Column(db.String(), nullable= True)
    phone_number = db.Column(db.Unicode(20), unique= True)
    country_code = db.Column(db.Unicode(8), unique= True)
    surgeons_name = db.Column(db.String(50))
    area = db.Column(db.String(255))
    report_problem = db.Column(db.String(255))
    date_record = db.Column(db.Date)

    phonenumber = db.orm.composite(
        PhoneNumber,
        phone_number,
        country_code
    )

    def __repr__(self):
        return '<id {}>'.format(self.id)

    class ReportForm(Form):
        opt_name = StringField('Name of person reporting')
        name = StringField('Initiate Name', [validators.Length(min=1, max=25)], validators=[DataRequired()])
        phone_number = PhoneNumberField(
            country_code='ZA' , display_format = 'international',
            validators=[DataRequired()]
        )
        surgeons_name = StringField('Surgeon Name', [validators.Length(min=1, max=25)], validators=[DataRequired()])
        area = StringField('Area of the problem', [validators.Length(min=1, max=25)], validators=[DataRequired()])
        report_problem = StringField('Area of the problem', [validators.Length(min=1, max=25)], validators=[DataRequired()])

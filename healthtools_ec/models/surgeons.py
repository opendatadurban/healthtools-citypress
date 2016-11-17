from ..app import db
from ..forms import Form
from wtforms import StringField, validators
from healthtools_ec.app import db


class Surgeon(db.Model):
    __tablename__ = 'surgeons'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    id_number = db.Column(db.String(50), nullable=True)
    area = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(10), nullable=True)
    standard = db.Column(db.String(10), nullable=True)
    category = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class RegisterForm(Form):
    class Meta:
        model = Surgeon
    name = StringField('Initiate Name', [validators.Length(max=50), validators.DataRequired()])
    phone_number = StringField('Phone Number', [validators.Length(min=10, max=10), validators.DataRequired()])
    area = StringField('Area where you work in', [validators.Length(max=255), validators.DataRequired()])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def validate(self):
        return super(RegisterForm, self).validate()

    def populate_obj(self, obj):
        super(RegisterForm, self).populate_obj(obj)


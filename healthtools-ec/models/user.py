from ..app import db, app
from ..forms import Form
from flask_mako import render_template

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import relationship
from flask_security import UserMixin, RoleMixin, Security, SQLAlchemyUserDatastore, LoginForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, InputRequired


class User(db.Model, UserMixin):
    """
    A user who can login and use Gibela.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), index=True, nullable=False, unique=True)
    password = Column(String(100), default='')
    # user_name = Column(String(50), nullable=False)
    admin = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)
    # phone = Column(String(10), default='')

    created_at = Column(DateTime(timezone=True), index=True, unique=False, nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())

    # associations
    # rides = db.relationship('Rider', backref=db.backref('riders', lazy='dynamic'), lazy='dynamic')
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return "<User phone=%s>" % (self.phone,)

    # Flask-Security requires an active attribute
    @property
    def active(self):
        return not self.disabled

    @active.setter
    def active(self, value):
        self.disabled = not value

    @classmethod
    def create_defaults(self):
        from flask_security.utils import encrypt_password

        admin_user = User()
        admin_user.admin = True
        admin_user.email = "admin@code4sa.org"
        admin_user.password = encrypt_password('admin')
        return [admin_user]


class Role(db.Model, RoleMixin):
    """
        A user who can login and use Gibela.
    """
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return unicode(self.name)

    @classmethod
    def create_defaults(self):
        return [
            Role(name='rider', description='user can supply ride information and request rides in return'),
            Role(name='provider', description='user can bid for and provide services'),
        ]


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE')))


class LoginForm(LoginForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


# user authentication
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, login_form=LoginForm)
app.extensions['security'].render_template = render_template

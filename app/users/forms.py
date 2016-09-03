
from flask_wtf import Form
from wtforms import TextField, validators
from wtforms.validators import Required

__all__ = ['GetByEmail']


class GetByEmail(Form):
    email = TextField('Email', validators=[Required()])

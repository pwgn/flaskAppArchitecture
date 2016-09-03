
from flask import Blueprint, request
from flask_login import current_user

from ..core import AppFormError
from ..forms import GetByEmail
from ..services import users
from . import route

bp = Blueprint('users', __name__, url_prefix='/users')


@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""
    return current_user._get_current_object()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)

@route(bp, '/email', methods=['POST'])
def find_user_with_email():
    form = GetByEmail()
    if form.validate_on_submit():
        return users.find(email = request.json['email']).first()
    raise AppFormError(form.errors)

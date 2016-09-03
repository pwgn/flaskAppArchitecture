from flask import Blueprint, render_template, request

from ..forms import GetByEmail
from . import route

bp = Blueprint('dashboard', __name__)


@route(bp, '/')
def index():
    form = GetByEmail()
    if form.validate_on_submit():
        return request.json
    return render_template('index.html', form=form)

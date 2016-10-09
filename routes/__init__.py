from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session
from flask import url_for
from flask import abort

from functools import wraps

from .user import current_user


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        print('admin required')
        if str(current_user().id) != '1':
            print('user id:', current_user().id)
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function
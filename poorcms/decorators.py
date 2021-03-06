from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user


def admin_required(f):
    '''
    Restrict access to admin group.
    '''
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.role == 'admin':
            return f(*args, **kwargs)
        else:
            flash('You need to be an admin to view this page.')
            return redirect(url_for('index'))
    return wrap

"""
All custom login and logout apis are defined here.
"""
from flask import redirect, url_for, request, session, render_template, flash, jsonify, abort
from flask_login import current_user, login_required, login_user, logout_user
from .. import db
from ..models import User, Permission, Role
from . forms import LoginForm
from . import auth

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    print('Login')
    if form.validate_on_submit():
        print('On Submit')
        user = User.query.filter_by(email=form.email.data).first()
        users = User.query.all()
        if user is not None and user.verify_password(form.password.data):
            print('successfully logged in')
            if (login_user(user, remember=form.remember_me.data) is False):
                return abort(403)
            flash('Successfully logged in.')
            return redirect(request.args.get('next') or url_for('main.index'))
        print('Unsuccessfull')
        flash('Invalid username or password.')
    return render_template('signin.html', loginform=form)

@auth.route('/logout', methods=['GET'])
def logout():
    """
    login uses flask-oauthlib api's. But logout is defined here
    for both fb and twitter.
    """
    logout_user()
    return redirect(url_for('main.index'))

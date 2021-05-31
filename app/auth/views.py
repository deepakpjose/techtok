"""
All custom login and logout apis are defined here.
"""
import os
from flask import redirect, url_for, request, session, render_template, flash, jsonify, abort
from flask_login import current_user, login_required, login_user, logout_user
from app import db, app 
from app.auth import auth
from app.models import User, Permission, Role, Post, PostType
from werkzeug.utils import secure_filename
from app.auth.forms import LoginForm, PosterCreateForm
from app.auth.decorators import permission_required
from app.auth.utils import allowed_file

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        users = User.query.all()

        if user is not None and user.verify_password(form.password.data):
            if (login_user(user, remember=form.remember_me.data) is False):
                return abort(403)
            flash('Successfully logged in.')
            return redirect(request.args.get('next') or url_for('main.index'))
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

def poster_directory_update(post, f):
    directory = '{:s}/{:s}'.format(app.config['UPLOAD_FOLDER'], str(post.id))
    uploaded_file_path = os.path.join(directory, f.filename)
    f.save(uploaded_file_path)

    uploaded_file_url = url_for('main.download_file', id=post.id, filename=f.filename)
    post.doc = uploaded_file_path
    post.url = uploaded_file_url
    return

@auth.route('/writeposters', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.WRITE_ARTICLES)
def writeposters():
    posterform = PosterCreateForm()

    if posterform.validate_on_submit():
        header = posterform.header.data
        body = posterform.body.data
        description = posterform.desc.data
        tags = posterform.tags.data
        f = posterform.poster.data
        filename = secure_filename(f.filename)

        if filename and allowed_file(filename):
            try:
                post = Post(body=body, header=header, description=description, tags=tags, \
                            post_type=PostType.POSTER)
            except:
                return render_template('error.html', msg="Poster creation failed")

            db.session.add(post)
            db.session.commit()

            directory = '{:s}/{:s}'.format(app.config['UPLOAD_FOLDER'], str(post.id))
            print('directory:{:s} id={:s}', directory, post.id)
            try:
                os.mkdir(directory)
            except:
                return render_template('error.html', msg="Poster directory creation failed")

            poster_directory_update(post, f)

            db.session.add(post)
            db.session.commit()

            flash('Created post')
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Failed creating post')
        return redirect(url_for('auth.writeposters'))

    return render_template('writeposter.html', posterform=posterform)

@auth.route('/editposters/<int:id>', methods=['GET', 'POST'])
@login_required
@permission_required(Permission.WRITE_ARTICLES)
def editposters(id):
    posterform = PosterCreateForm()

    if posterform.validate_on_submit():
        header = posterform.header.data
        body = posterform.body.data
        description = posterform.desc.data
        tags = posterform.tags.data
        f = posterform.poster.data
        filename = secure_filename(f.filename)

        if filename and allowed_file(filename):
            try:
                post = Post.query.get_or_404(id)
                post.body = body
                post.header = header
                post.description = description
                post.tags = tags
                post.post_type = PostType.POSTER
            except:
                msg = "Poster editing failed: {:s}".format(sys.exc_info()[0])
                return render_template('error.html', msg=msg)

            poster_directory_update(post, f)

            db.session.add(post)
            db.session.commit()
            flash('Edited post')
            return redirect(request.args.get('next') or 
                            url_for('main.post', id=post.id, header=post.header))

        flash('Failed finding post')
        return redirect(url_for('auth.writeposters'))

    return render_template('writeposter.html', posterform=posterform)

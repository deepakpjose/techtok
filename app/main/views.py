from flask import render_template, url_for
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html') 

@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    return render_template('post.html')

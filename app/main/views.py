from flask import render_template, session, redirect, \
                  url_for, current_app, request, flash, abort, jsonify, make_response
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return 'hello techzines.com'

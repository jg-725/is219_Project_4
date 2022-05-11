from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

starter_pages = Blueprint('starter_pages', __name__,
                        template_folder='templates')


@starter_pages.route('/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@starter_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@starter_pages.route('/welcome')
def welcome():
    try:
        return render_template('welcome.html')
    except TemplateNotFound:
        abort(404)
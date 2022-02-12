from django import views
from flask import Flask


my_app = Flask(__name__)
my_app.config['SECRET_KEY'] = '0961691511722547'

import app.views

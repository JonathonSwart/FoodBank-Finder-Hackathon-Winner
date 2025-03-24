"""
The main file we will be using to manage the application and the 
database.
"""

from flask import Flask
import os


app = Flask(__name__)
db_string = os.getenv('db_string')
if db_string:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_string
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '69c0e04z04756x65eabcg2c5a11c8524'
app.app_context().push()

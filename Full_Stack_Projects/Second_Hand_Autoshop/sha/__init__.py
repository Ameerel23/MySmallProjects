import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sha.db')

db = SQLAlchemy(app)

from sha import routes

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Instantiate flask object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'e3d853eac44f510167d6d586'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes
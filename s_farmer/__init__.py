from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menuinfor.db'
app.config['SECRET_KEY'] = 'graceJosphat'
db = SQLAlchemy(app)

from s_farmer import routes

from flask import Flask
# imported sqlalchemy
from flas.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)


from app import views, models


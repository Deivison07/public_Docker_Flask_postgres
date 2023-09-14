from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from common.settings import DATABASE_CONNECTION_URL

db = SQLAlchemy()

def config_database(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

def get_engine():
    return create_engine(DATABASE_CONNECTION_URL)
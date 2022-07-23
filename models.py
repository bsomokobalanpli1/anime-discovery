"""
import
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin



# pylint: disable=no-member
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

db = SQLAlchemy()




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
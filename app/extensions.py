"""Extensions module - Set up for additional libraries can go in here."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    events = db.relationship('Event', backref='author', lazy='True')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    start_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Event({self.id}, '{self.title}')"
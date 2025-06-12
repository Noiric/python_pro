from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    course = db.Column(db.String(100))
    photo_url = db.Column(db.String(255))

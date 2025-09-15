from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    course = db.Column(db.String(100))
    photo_url = db.Column(db.String(255))
    phone_number = db.Column(db.String(20), nullable=True)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    tax_code = db.Column(db.String(64), nullable=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    @staticmethod
    def get_instance():
        return Company.query.first()


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    learning_plan = db.Column(db.Text, nullable=True)

    def __str__(self):
        return self.name

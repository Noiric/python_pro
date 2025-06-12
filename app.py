from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/health')
def health_check():
    return '', 200


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students')
def get_students():
    name = request.args.get('name', '')
    students = Student.query.filter(Student.name.ilike(f"%{name}%")).all()
    return jsonify([
        {
            'id': s.id,
            'name': s.name,
            'birthdate': s.birthdate.isoformat(),
            'course': s.course,
            'photo_url': s.photo_url,
            'age': calculate_age(s.birthdate)
        } for s in students
    ])


def calculate_age(birthdate):
    today = date.today()
    return today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )


if __name__ == '__main__':
    app.run(debug=True)

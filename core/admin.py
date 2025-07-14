from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, Student
from django.contrib import admin
from .models import Department, Position


def setup_admin(app):
    admin = Admin(app, name="Адмінка", template_mode="bootstrap4")
    admin.add_view(ModelView(Student, db.session))


admin.site.register(Department)
admin.site.register(Position)

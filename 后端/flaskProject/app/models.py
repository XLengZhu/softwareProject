from . import db

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    permission = db.Column(db.Boolean, nullable=False, default=False)

class Administrator(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Classroom(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)

class ClassroomUsage(db.Model):
    classroom_id = db.Column(db.String(50), db.ForeignKey('classroom.id'), primary_key=True)
    start_time = db.Column(db.DateTime, primary_key=True)
    end_time = db.Column(db.DateTime, primary_key=True)
    occupier_id = db.Column(db.String(50), nullable=False)
    classroom = db.relationship('Classroom', backref=db.backref('usages', lazy=True))
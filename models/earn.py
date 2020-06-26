from app import db
import datetime


class Earn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_cpf = db.Column(db.String(30), db.ForeignKey('person.cpf'), nullable=False)
    value = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __init__(self, person_cpf, value, description):
        self.person_cpf = person_cpf
        self.value = value
        self.description = description
from app import db


class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_cpf = db.Column(db.String(30), db.ForeignKey('person.cpf'), nullable=False)
    company = db.Column(db.String(20), nullable=False)
    expiration = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __init__(self, person_cpf, company, expiration, value):
        self.person_cpf = person_cpf
        self.company = company
        self.expiration = expiration
        self.value = value

from app import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_cpf = db.Column(db.String(30), db.ForeignKey('person.cpf'), nullable=False)
    card_number = db.Column(db.String(20), nullable=False)
    card_company = db.Column(db.String(20), nullable=False)
    limit = db.Column(db.Float, nullable=False)
    card_statement = db.Column(db.Float, nullable=False)

    def __init__(self, person_cpf, card_number, card_company, limit, card_statement):
        self.person_cpf = person_cpf
        self.card_number = card_number
        self.card_company = card_company
        self.limit = limit
        self.card_statement = card_statement


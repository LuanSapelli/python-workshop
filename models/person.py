from app import db


class Person(db.Model):
    name = db.Column(db.String(150))
    cpf = db.Column(db.String(30), primary_key=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    debts = db.relationship('Debt')
    cards = db.relationship('Card')
    earn = db.relationship('Earn')
    spent = db.relationship('Spent')

    def __init__(self, name, cpf, password, email):
        self.name = name
        self.cpf = cpf
        self.password = password
        self.email = email

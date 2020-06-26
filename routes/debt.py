from models.debt import Debt
from models.person import Person
from flask import request, jsonify
from app import app, db


@app.route('/debt')
def get_all_debt():
    debts = Debt.query.all()

    result = []
    for debt in debts:
        data = {}
        data['id'] = debt.id
        data['person_cpf'] = debt.person_cpf
        data['company'] = debt.company
        data['expiration'] = debt.expiration
        data['value'] = debt.value

        result.append(data)

    return jsonify(result)


@app.route('/debt/<id>', methods=['GET'])
def get_debt(id):
    debt = Debt.query.get(id)

    result = {
        'id': debt.id,
        'person_cpf': debt.person_cpf,
        'company': debt.company,
        'expiration': debt.expiration,
        'value': debt.value
    }

    return jsonify(result)


@app.route('/debt', methods=['POST'])
def insert_debt():
    person_cpf = request.json['person_cpf']
    company = request.json['company']
    expiration = request.json['expiration']
    value = request.json['value']

    debt = Debt(person_cpf, company, expiration, value)
    db.session.add(debt)
    db.session.commit()

    return "Dívida inserida com sucesso!"


@app.route('/debt', methods=['PUT'])
def update_debt():
    id = request.json['id']
    debt = Debt.query.get(id)
    debt.person_cpf = request.json['person_cpf']
    debt.company = request.json['company']
    debt.expiration = request.json['expiration']
    debt.value = request.json['value']

    db.session.commit()

    return "Dívida atualizada com sucesso!"


@app.route('/debt/<id>', methods=['DELETE'])
def delete_debt(id):
    debt = Debt.query.get(id)

    db.session.delete(debt)
    db.session.commit()

    return "Dívida deletada com sucesso!"


@app.route('/person/debt/<person_cpf>', methods=['GET'])
def get_person_debts(person_cpf):
    person = Person.query.get(person_cpf)

    debts = person_debts(person.debts)

    return jsonify(debts)


def person_debts(debts):
    result = []

    for debt in debts:
        data = {}

        data['id'] = debt.id
        data['person_cpf'] = debt.person_cpf
        data['company'] = debt.company
        data['expiration'] = debt.expiration
        data['value'] = debt.value

        result.append(data)
    return result

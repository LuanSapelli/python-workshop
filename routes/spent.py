from models.spent import Spent
from models.person import Person
from flask import request, jsonify
from app import app, db


@app.route('/spent', methods=['POST'])
def insert_spent():
    person_cpf = request.json['person_cpf']
    value = request.json['value']
    description = request.json['description']

    spent = Spent(person_cpf, value, description)
    db.session.add(spent)
    db.session.commit()

    return "Gasto inserido com sucesso!"


@app.route('/spent/<id>', methods=['DELETE'])
def delete_spent(id):
    spent = Spent.query.get(id)

    db.session.delete(spent)
    db.session.commit()

    return "Gasto deletado com sucesso!"


@app.route('/person/spent/<person_cpf>', methods=['GET'])
def get_person_spent(person_cpf):
    person = Person.query.get(person_cpf)

    spent = person_spent(person.spent)

    return jsonify(spent)


def person_spent(spents):
    result = []

    for spent in spents:
        data = {}

        data['id'] = spent.id
        data['person_cpf'] = spent.person_cpf
        data['value'] = spent.value
        data['description'] = spent.description
        data['date'] = spent.date

        result.append(data)
    return result

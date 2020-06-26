from models.earn import Earn
from models.person import Person
from flask import request, jsonify
from app import app, db


@app.route('/earnings', methods=['POST'])
def insert_earn():
    person_cpf = request.json['person_cpf']
    value = request.json['value']
    description = request.json['description']

    earn = Earn(person_cpf, value, description)
    db.session.add(earn)
    db.session.commit()

    return "Ganho inserido com sucesso!"


@app.route('/earnings/<id>', methods=['DELETE'])
def delete_earn(id):
    earn = Earn.query.get(id)

    db.session.delete(earn)
    db.session.commit()

    return "Ganho deletado com sucesso!"


@app.route('/person/earnings/<person_cpf>', methods=['GET'])
def get_person_earn(person_cpf):
    person = Person.query.get(person_cpf)

    earns = person_earns(person.earn)

    return jsonify(earns)


def person_earns(earns):
    result = []

    for earn in earns:
        data = {}

        data['id'] = earn.id
        data['person_cpf'] = earn.person_cpf
        data['value'] = earn.value
        data['description'] = earn.description
        data['date'] = earn.date

        result.append(data)
    return result

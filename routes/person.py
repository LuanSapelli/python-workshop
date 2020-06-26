from models.person import Person
from flask import request, jsonify
from app import app, db


@app.route('/person')
def get_all_person():
    people = Person.query.all()

    result = []
    for person in people:
        data = {}
        data['name'] = person.name
        data['cpf'] = person.cpf
        data['password'] = person.password
        data['email'] = person.email

        result.append(data)

    return jsonify(result)


@app.route('/person/<cpf>', methods=['GET'])
def get_person(cpf):
    person = Person.query.get(cpf)

    result = {
        'name': person.name,
        'cpf': person.cpf,
        'password': person.password,
        'email': person.email
    }

    return jsonify(result)


@app.route('/person', methods=['POST'])
def insert_person():
    name = request.json['name']
    cpf = request.json['cpf']
    password = request.json['password']
    email = request.json['email']

    person = Person(name, cpf, password, email)
    db.session.add(person)
    db.session.commit()

    return "Pessoa inserida com sucesso!"


@app.route('/person', methods=['PUT'])
def update_person():
    cpf = request.json['cpf']
    person = Person.query.get(cpf)
    person.name = request.json['name']
    person.cpf = request.json['cpf']
    person.email = request.json['email']

    db.session.commit()

    return "Pessoa atualizada com sucesso!"


@app.route('/person/<cpf>', methods=['DELETE'])
def delete_person(cpf):
    person = Person.query.get(cpf)

    db.session.delete(person)
    db.session.commit()

    return "Pessoa deletada com sucesso!"
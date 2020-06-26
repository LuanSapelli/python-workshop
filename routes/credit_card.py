from models.credit_card import Card
from models.person import Person
from flask import request, jsonify
from app import app, db


@app.route('/card/<id>', methods=['GET'])
def get_card(id):
    card = Card.query.get(id)

    result = {
        'id': card.id,
        'person_cpf': card.person_cpf,
        'card_number': card.card_number,
        'card_company': card.card_company,
        'limit': card.limit,
        'card_statement': card.card_statement
    }

    return jsonify(result)


@app.route('/card', methods=['POST'])
def insert_card():
    person_cpf = request.json['person_cpf']
    card_number = request.json['card_number']
    card_company = request.json['card_company']
    limit = request.json['limit']
    card_statement = request.json['card_statement']

    card = Card(person_cpf, card_number, card_company, limit, card_statement)
    db.session.add(card)
    db.session.commit()

    return "Cartão inserido com sucesso!"


@app.route('/card', methods=['PUT'])
def update_card():

    id = request.json['id']

    card = Card.query.get(id)

    card.person_cpf = request.json['person_cpf']
    card.card_number = request.json['card_number']
    card.card_company = request.json['card_company']
    card.limit = request.json['limit']
    card.card_statement = request.json['card_statement']

    db.session.commit()

    return "Cartão atualizado com sucesso!"


@app.route('/card/<id>', methods=['DELETE'])
def delete_card(id):
    card = Card.query.get(id)

    db.session.delete(card)
    db.session.commit()

    return "Cartão deletado com sucesso!"


@app.route('/person/card/<person_cpf>', methods=['GET'])
def get_person_cards(person_cpf):
    person = Person.query.get(person_cpf)

    cards = person_cards(person.cards)

    return jsonify(cards)


def person_cards(cards):
    result = []

    for card in cards:
        data = {}

        data['id'] = card.id
        data['person_cpf'] = card.person_cpf
        data['card_number'] = card.card_number
        data['card_company'] = card.card_company
        data['limit'] = card.limit
        data['card_statement'] = card.card_statement

        result.append(data)
    return result

from flask import Blueprint, request, jsonify

from .schemas import EntradaSchema
from .models import Entrada
from app.configuracao.db import db


entrada = Blueprint('entrada', __name__)


@entrada.route('/', methods=['GET'])
def get_entradas():
    entrada_esquema = EntradaSchema(many=True)
    entradas = Entrada.query.filter(Entrada.is_bet == False)
    return jsonify(entrada_esquema.dump(entradas)), 200 


@entrada.route('/<int:id>/', methods=['PUT'])
def make_entrada_bet(id):
    entrada = Entrada.query.get(id)
    entrada.is_bet = True

    db.session.commit()

    return jsonify({
        "success": True
    }), 201


@entrada.route('/', methods=['PUT'])
def make_entradas_bet():
    ids = request.json.get("ids", [])
    
    for id in ids:
        entrada = Entrada.query.get(id)
        entrada.is_bet = True
    
    db.session.commit()

    return jsonify({
        "success": True
    }), 201


@entrada.route('/', methods=['POST'])
def create_entrada():
    entrada_schema = EntradaSchema()
    
    try:
        print(request.json)
        entrada = Entrada(**request.json)
        
        db.session.add(entrada)
        db.session.commit()
        
        data = {
            'message': 'Entrada adicionada com sucesso',
            'data': entrada_schema.dump(entrada)
        }

        return jsonify(data), 201

    except(ValueError, TypeError):
        data = {
            'message': 'Erro ao adicionar entrada'
        }

        return jsonify(data), 400


@entrada.route("/<int:id>/",methods=['DELETE'])
def entrada_deletar(id):
    dados = {}

    try:
        entrada = Entrada.query.get(id)

        db.session.delete(entrada)
        db.session.commit()

        autorschema = EntradaSchema()
        
        dados["data"] = autorschema.dump(entrada)
        dados["mensagem"] = "Autor deletado com sucesso!"

        return jsonify(dados)
    except: 
        dados["mensagem"] = "Impossivel excluir autor, verificar dados."
        return jsonify(dados)
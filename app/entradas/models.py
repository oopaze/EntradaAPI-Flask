from datetime import datetime

from app.configuracao.db import db


class Entrada(db.Model):
    __tablename__ = 'entradas'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    valor = db.Column(db.Integer, default=5)
    criador = db.Column(db.String)
    is_bet = db.Column(db.Boolean, default=False)
    criado_em = db.Column(db.DateTime, default=datetime.now)


    def __init__(self, link, criador, valor=5, is_bet=False):
        self.link = link
        self.valor = valor
        self.is_bet = is_bet
        self.criador = criador

    def __repr__(self):
        return f"{self.id} - {self.link} ({self.criador})"
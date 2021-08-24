from app.configuracao.ma import ma
from .models import Entrada


class EntradaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Entrada
        fields = (
            "id",
            "link",
            "valor",
            "criador",
            "is_bet",
            "criado_em",
        )
from app.configuracao.ma import ma
from .models import Entrada


class EntradaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Entrada
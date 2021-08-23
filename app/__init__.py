from flask_migrate import Migrate
from flask import Flask

from .configuracao.db import configure_db
from .configuracao.ma import configure_ma
from .configuracao.auth import configure_auth

from .src.routes import src
from .entradas.routes import entrada

def create_app():
    """Função responsável por configurar e criar a Flask App"""
    app = Flask(__name__)

    app.config.from_object('config.Development')

    configure_db(app)
    configure_ma(app)
    configure_auth(app)

    Migrate(app, app.db)

    app.register_blueprint(src)
    app.register_blueprint(entrada, url_prefix='/entrada')

    return app

app = create_app()

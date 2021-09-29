from flask import Flask
from datetime import timedelta

def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///experimento_seguridad.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(days=1)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app
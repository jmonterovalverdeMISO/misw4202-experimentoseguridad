from flask import Flask
from datetime import timedelta

def create_app(config_name):
    app = Flask(__name__)  
    app.config['JWT_SECRET_KEY']='frase-secreta'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(days=1)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app
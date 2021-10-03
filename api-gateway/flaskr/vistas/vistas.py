from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
from datetime import datetime
import json


class VistaHistoriaClinica(Resource):

    @jwt_required()
    def get(self):
        return request.get('https://api.github.com')
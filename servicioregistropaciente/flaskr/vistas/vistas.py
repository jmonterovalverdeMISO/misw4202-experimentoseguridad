from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token
from datetime import datetime
import json


class VistaRegistroPaciente(Resource):

    @jwt_required()
    def get(self, id_usuario):
        return "consulta ejecutada", 200

    @jwt_required()
    def post(self, id_usuario):
        return "Modificación ejecutada", 200
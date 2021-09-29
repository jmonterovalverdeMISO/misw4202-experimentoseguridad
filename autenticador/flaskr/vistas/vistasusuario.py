from .helper import Helper
from flask import request
from ..modelos import Usuario, UsuarioSchema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token
from ..modelos import db

usuario_schema = UsuarioSchema()
helper = Helper()

class VistaSignIn(Resource):
    
    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"], contrasena=request.json["contrasena"])
        db.session.add(nuevo_usuario)
        db.session.commit()
        token_de_acceso = create_access_token(
            identity = {"id": nuevo_usuario.id, "name": nuevo_usuario.nombre}
        )
        return {
            "mensaje":"usuario creado exitosamente",
            "token":token_de_acceso
        }


    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena",usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '',204

class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.nombre == request.json["nombre"], Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(
                identity = {"id": usuario.id, "name": usuario.nombre}
            )
            return {
                "mensaje":"Inicio de sesión exitoso",
                "token": token_de_acceso
            }
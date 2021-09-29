from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required

class Helper():
     @jwt_required()
     def getIdUsuario(self):
        jwt = get_jwt_identity()
        id_usuario = jwt.get("id")
        return id_usuario
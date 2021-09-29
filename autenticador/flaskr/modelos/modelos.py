from flask_sqlalchemy import SQLAlchemy, model
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Usuario
         include_relationships = True
         load_instance = True

class UsuarioSimpleSchema(SQLAlchemyAutoSchema):
    class Meta:
         #model = Usuario
         fields = ('id','nombre')
         include_relationships = True
         load_instance = True
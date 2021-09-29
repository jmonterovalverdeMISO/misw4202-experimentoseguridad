from flaskr import create_app
from flask_restful import Api
from flaskr.modelos.modelos import db
from flaskr.vistas.vistasusuario import VistaSignIn,VistaLogIn
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/logIn')

jwt = JWTManager(app)




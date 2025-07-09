from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
api = Api(
    title='ToDo API',
    version='1.0',
    description='Swagger UI for ToDo backend',
    doc='/swagger'
)
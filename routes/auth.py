from flask import request
from flask_jwt_extended import create_access_token
from flask_restx import Namespace, fields, Resource

from ..app.extensions import db
from app.models import Users

auth_ns = Namespace('auth', description='Authentication related operations')

singup_model = auth_ns.model('SingUp', {
    "username": fields.String(required=True),
    "password": fields.String(required=True)
})

auth_ns.route("/singup")
class SingUp(Resource):
    @auth_ns.expect(singup_model)
    def post(self):
        data = request.json
        user = Users(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully"}, 201

@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(singup_model)
    def post(self):
        data = request.json
        user = Users.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.id)
            return {"access_token": token}, 200
        return {"message": "Invalid credentials"}, 401
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, fields, Resource

from app import db

tasks_ns = Namespace('todos', description='Task management')

task_model = tasks_ns.model('Task', {
    "title": fields.String(required=True),
    "description": fields.String
})

@tasks_ns.route("")
class Tasks(Resource):
    @jwt_required()
    @tasks_ns.marshal_list_with(task_model)
    def get(self):
        user_id = get_jwt_identity()
        return Tasks.query.filter_by(user_id=user_id).all()

    @jwt_required()
    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model, code=201)
    def post(self):
        data = tasks_ns.payload
        task = Tasks(title=data['title'], description=data['description'])
        task.user_id = get_jwt_identity()
        db.session.add(task)
        db.session.commit()
        return task, 201
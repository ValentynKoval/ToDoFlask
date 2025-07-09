from flask import Flask

from app.config import Config
from app.extensions import migrate, api, jwt, db
from routes.auth import auth_ns
from routes.todos import tasks_ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(tasks_ns, path='/todos')

    return app
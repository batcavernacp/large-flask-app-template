from flask import Flask
from config import Config

from app.extensions.restful import setup_restful
from app.extensions.database import db
# from app.extensions.swagger import setup_swagger

from app.seed import seed

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed()

    setup_restful(app)
    
    # setup_swagger(app)

    @app.route('/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

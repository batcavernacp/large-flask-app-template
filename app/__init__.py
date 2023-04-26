from flask import Flask
from flask_restful import Api
from config import Config
from app.extensions import db
from app.routes import setup_api
from app.seed import seed

def create_app(config_class=Config):
    app = Flask(__name__)

    api = Api(app)

    app.config.from_object(config_class)

    db.init_app(app)
    
    setup_api(api)

    with app.app_context():
        db.drop_all()
        db.create_all()
        seed()

    @app.route('/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

from flask import Flask, jsonify

from config import Config
from app.extensions import db
from app.routes import create
from app.seed import seed



def create_app(config_class=Config):
    app = Flask(__name__)

    # @app.after_request
    # def after(response):
    #     if response.data and not response.is_json:
    #         response.data = jsonify(response.get_json())
    #         response.content_type = 'application/json'
    #     return response

    app.config.from_object(config_class)

    db.init_app(app)
    
    create(app)

    with app.app_context():
        db.drop_all()
        db.create_all()
        seed()

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

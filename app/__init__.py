from flask import Flask

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    from app.routes import posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.routes import questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    with app.app_context():
        db.create_all()

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

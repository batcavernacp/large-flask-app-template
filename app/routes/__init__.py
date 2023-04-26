from flask import Blueprint, jsonify

posts_bp = Blueprint('posts', __name__)
import app.routes.posts


questions_bp = Blueprint('questions', __name__)
import app.routes.questions 

def create(app):
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(questions_bp, url_prefix='/questions')

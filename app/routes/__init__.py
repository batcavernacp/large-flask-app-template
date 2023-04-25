from flask import Blueprint

posts_bp = Blueprint('posts', __name__)
import app.routes.posts


questions_bp = Blueprint('questions', __name__)
import app.routes.questions 

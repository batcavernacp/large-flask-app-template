from app.routes.posts import Posts
from app.routes.questions import Questions
from flask_restful import Api

def setup_api(api: Api):
    api.add_resource(Posts, '/posts', '/posts/<int:id>')
    api.add_resource(Questions, '/questions', '/questions/<int:id>')

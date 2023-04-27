from flask_restful import Api
from app.routes.posts import Posts
from app.routes.questions import Questions
from flask import Flask

def setup_restful(app: Flask):
    api = Api(app)
    api.add_resource(Posts, '/posts', '/posts/<int:id>')
    api.add_resource(Questions, '/questions', '/questions/<int:id>')

    return api

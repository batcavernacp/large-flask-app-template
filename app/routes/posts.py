from flask_restful import Resource, reqparse
from app.services.posts import get_posts, create_post, edit_post, delete_post, get_post

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Title of the post')
parser.add_argument('content', type=str, help='Content of the post')

class Posts(Resource):
    def get(self, id=None):
        if id:
            return get_post(id).serialize()
        return [post.serialize() for post in get_posts()]

    def post(self):
        args = parser.parse_args()
        new_post = create_post(args)
        return new_post.serialize()
        
    def put(self, id):
        args = parser.parse_args()
        return edit_post(id, args).serialize()

    def delete(self, id):
        return delete_post(id).serialize()
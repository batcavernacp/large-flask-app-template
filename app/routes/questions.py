from flask_restful import Resource, reqparse
from app.services.questions import get_questions, get_question, create_question, edit_question, delete_question

parser = reqparse.RequestParser()
parser.add_argument('content', type=str, help='Content of the question')
parser.add_argument('answer', type=str, help='Answer of the question')

class Questions(Resource):
    def get(self, id=None):
        if id:
            return get_question(id).serialize()
        return [question.serialize() for question in get_questions()]

    def post(self):
        args = parser.parse_args()
        new_question = create_question(args)
        return new_question.serialize()
    
    def put(self, id):
        args = parser.parse_args()
        return edit_question(id, args).serialize()

    def delete(self, id):
        return delete_question(id).serialize()

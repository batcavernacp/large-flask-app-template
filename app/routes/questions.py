from flask import request, json
from app.routes import questions_bp as bp
from app.models.question import Question
from app.extensions import db

@bp.get('/')
def list():
    questions = Question.query.all()
    return questions

@bp.post('/')
def index():
    data = json.loads(request.data)
    new_question = Question(content=data.get('content'),
                            answer=data.get('answer'))
    db.session.add(new_question)
    db.session.commit()
    return new_question.serialize()

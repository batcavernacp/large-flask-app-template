from app.models.question import Question
from app.extensions.database import db

def get_questions():
    return Question.query.all()

def get_question(id):
    return Question.query.get(id)

def create_question(request):
    content = request['content']
    answer = request['answer']
    new_question = Question(content=content, answer=answer)
    db.session.add(new_question)
    db.session.commit()

    return new_question

def edit_question(id, request):
    question = Question.query.get(id)
    question.content = request['content']
    question.answer = request['answer']
    db.session.commit()
    return question

def delete_question(id):
    question = Question.query.get(id)
    question.deleted = True
    db.session.commit()
    return question
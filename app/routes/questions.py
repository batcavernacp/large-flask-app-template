from flask import request
from app.routes import questions_bp as bp
from app.models.question import Question
from app.extensions import db

@bp.route('/', methods=('GET', 'POST'))
def index():
    questions = Question.query.all()

    if request.method == 'POST':
        new_question = Question(content=request.form['content'],
                                answer=request.form['answer'])
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions.index'))

    return questions


from models.comment import Comment as Model
from routes import *


main = Blueprint('comment', __name__)


# @main.route('/')
# def index():
#     ms = Model.query.all()
#     return render_template('node_index.html', node_list=ms)


# @main.route('/edit/<id>')
# def edit(id):
#     m = Model.query.filter_by(id=id).first()
#     return render_template('todo_edit.html', todo=m)


# @main.route('/<int:id>')
# def show(id):
#     m = Model.query.get(id)
#     return render_template('node.html', node=m)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('topic.show', id=m.topic_id))


@main.route('/delete/<id>')
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return redirect(url_for('topic.show', id=m.topic_id))


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     m = Model.query.get(id)
#     m.update(form)
#     return redirect(url_for('.index'))




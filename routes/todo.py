from models.todo import Todo as Model
from routes import *


main = Blueprint('todo', __name__)


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('todo_index.html', todo_list=ms)


@main.route('/edit/<id>')
def edit(id):
    m = Model.query.filter_by(id=id).first()
    return render_template('todo_edit.html', todo=m)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.query.get(id)
    m.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return redirect(url_for('.index'))

from models.topic import Topic
from models.user import User
from routes import *
from routes.user import current_user


Model = Topic

main = Blueprint('topic', __name__)


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('topic_index.html', topic_list=ms)


# @main.route('/edit/<id>')
# def edit(id):
#     m = Model.query.filter_by(id=id).first()
#     return render_template('todo_edit.html', todo=m)

@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    u = current_user()
    return render_template('topic.html', topic=m, user=u, User=User)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     m = Model.query.get(id)
#     m.update(form)
#     return redirect(url_for('.index'))


@main.route('/delete/<id>')
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return redirect(url_for('.index'))

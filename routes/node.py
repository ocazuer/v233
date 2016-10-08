from models.node import Node as Model
from models.user import User
from routes import *
from functools import wraps

main = Blueprint('node', __name__)


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        print('admin required')
        if request.args.get('uid') != '1':
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('node_index.html', node_list=ms, user=current_user())


# @main.route('/edit/<id>')
# def edit(id):
#     m = Model.query.filter_by(id=id).first()
#     return render_template('todo_edit.html', todo=m)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    return render_template('node.html', node=m, user=current_user(), User=User)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))
    # return render_template('node.html', node=m, user=current_user())


# @main.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     form = request.form
#     m = Model.query.get(id)
#     m.update(form)
#     return redirect(url_for('.index'))


@main.route('/delete/<id>')
@admin_required
def delete(id):
    m = Model.query.filter_by(id=id).first()
    m.delete()
    return redirect(url_for('.index'))

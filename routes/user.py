from models.user import User
from routes import *

Model = User

main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        u = User.query.get(uid)
        return u
    return None


@main.route('/')
def index():
    ms = Model.query.all()
    return render_template('user_index.html', user_list=ms, user=current_user())


# @main.route('/edit/<id>')
# def edit(id):
#     m = Model.query.filter_by(id=id).first()
#     return render_template('todo_edit.html', todo=m)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    return render_template('user.html', user=current_user())


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)

    if m.validate_register():
        m.save()
        return redirect(url_for('.index'))
    else:
        return render_template('user_error.html', user=current_user())


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


@main.route('/verification_login', methods=['POST'])
def verification_login():
    form = request.form
    u = Model(form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        print('登录成功')
        session['user_id'] = user.id
    else:
        print('登录失败')
    return redirect(url_for('index.index'))


@main.route('/login')
def login():
    return render_template('user_login.html', user=current_user())


@main.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index.index'))
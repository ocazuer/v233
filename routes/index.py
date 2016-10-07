from models.node import Node
from models.topic import Topic
from routes import *
from functools import wraps


main = Blueprint('index', __name__)


@main.route('/')
def index():
    ns = Node.query.all()
    ts = Topic.query.all()
    return render_template('index.html', node_list=ns, topic_list=ts, user=current_user())

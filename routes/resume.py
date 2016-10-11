from models.node import Node as Model
from models.user import User
from routes import *
from flask import make_response
from flask import send_file
main = Blueprint('download', __name__)


@main.route('/')
def index():
    return render_template('resume.html')


@main.route('/pdf')
def download():
    response = make_response(send_file("static/pdf/resume_v0.pdf"))
    response.headers["Content-Disposition"] = "attachment; filename=resume.pdf"
    return response
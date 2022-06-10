from flask import render_template, Blueprint


content = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content.route("/")
def home():
    return render_template("index.html")

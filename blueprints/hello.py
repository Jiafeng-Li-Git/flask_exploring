
from flask import Blueprint, render_template


hello_bp = Blueprint("hello", __name__)


@hello_bp.route("/hello/<user_name>")
def hello(user_name):

    # return f"Hello, {user_name}!"
    return render_template("hello.html", name=user_name)

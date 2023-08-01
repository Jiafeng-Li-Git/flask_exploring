
from flask import Blueprint, render_template, session, redirect

hello_bp = Blueprint("hello", __name__)


@hello_bp.route("/hello")
def hello():
    return render_template("hello.html", name=session.get("username"))

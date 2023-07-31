
from flask import Blueprint, render_template, request, url_for, redirect


login_bp = Blueprint("login", __name__)


@login_bp.get("/login")
def login_get():
    return render_template("login.html")


@login_bp.post("/login")
def login_post():
    username = request.form["username"]
    pwd = request.form["password"]
    if valid_user(username, pwd):
        hello_url = url_for("hello.hello", user_name=username)
        return redirect(hello_url)
    else:
        return "Invalid username/password!"


def valid_user(username, password):
    if username == "jli" and password == "666":
        return True
    else:
        return False


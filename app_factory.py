
import os
import uuid
from flask import Flask, request, session, redirect, abort


def get_secret_keys():
    key_string = os.getenv("SECRET_KEYS")
    keys = key_string.split(",")
    return keys


def get_api_keys():
    key_string = os.getenv("API_KEYS")
    keys = key_string.split(",")
    return keys


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration)
    app.config["SECRET_KEY"] = get_secret_keys()
    app.config["valid_api_keys"] = get_api_keys()

    @app.before_request
    def check_auth():

        if (
            request.endpoint == "login.login"
            or request.endpoint == "root.root"
        ):
            return None

        if request.endpoint == "hello.hello":
            if not session.get("username"):
                return redirect("login")
            return None

        def is_valid_uuid(val):
            try:
                uuid.UUID(str(val))
                return True
            except ValueError:
                return False

        if request.endpoint == "total_sales_value.total_sales_value":
            user_key = request.headers.get("X-Api-Key")
            if not user_key or not is_valid_uuid(user_key):
                app.logger.error("Empty or wrong format API key.")
                abort(401)
            else:
                if user_key in app.config["valid_api_keys"]:
                    app.logger.info("API keys authentication completed: valid api key.")
                    return None
                else:
                    app.logger.error("Wrong API key.")
                    abort(401)

    with app.app_context():
        from blueprints import (
            root,
            hello,
            login,
            total_sales_value,
        )

        app.register_blueprint(root.root_bp)
        app.register_blueprint(hello.hello_bp)
        app.register_blueprint(login.login_bp)
        app.register_blueprint(total_sales_value.total_sales_value_bp)

    return app

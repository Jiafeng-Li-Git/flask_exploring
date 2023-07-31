
from flask import Flask


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration)

    with app.app_context():
        from blueprints import (
            root,
            hello,
            login,
        )

        app.register_blueprint(root.root_bp)
        app.register_blueprint(hello.hello_bp)
        app.register_blueprint(login.login_bp)

    return app

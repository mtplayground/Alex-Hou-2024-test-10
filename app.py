from flask import Flask

from db import initialize_schema


def create_app() -> Flask:
    app = Flask(__name__)
    initialize_schema()
    return app


app = create_app()

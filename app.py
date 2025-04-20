# john_dorado/__init__.py
from flask import Flask, render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Example public route
    @app.route("/")
    def home():
        return render_template("index.html")


    return app

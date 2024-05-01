import os

from flask import Flask, render_template

from app.database import create_all, drop_all, Session


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config["SECRET_KEY"] = os.urandom(12).hex()

    from app.routes import default_bp
    app.register_blueprint(default_bp, url_prefix='/')

    from app import models
    create_all()


    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def handler(e):
        return render_template('error.html', code=e.code)

    return app
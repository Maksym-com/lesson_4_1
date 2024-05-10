import os

from flask import Flask, render_template
from flask_login import LoginManager

from app.database import create_all, drop_all, Session


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config["SECRET_KEY"] = os.urandom(12).hex()
    login_manager = LoginManager()
    login_manager.login_view = "login"
    login_manager.init_app(app)

    from app.routes import default_bp, user_bp, company_bp
    app.register_blueprint(default_bp, url_prefix='/')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(company_bp, url_prefix='/company')

    from app import models
    create_all()

    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(405)
    @app.errorhandler(500)
    def handler(e):
        return render_template('error.html', code=e.code)

    @login_manager.user_loader
    def load_user(user_id: int):
        with Session() as session:
            return session.query(models.User).where(models.User.id == user_id).first()

    @login_manager.user_loader
    def load_company(company_id: int):
        with Session() as session:
            return session.query(models.Company).where(models.Company.id == company_id).first()

    return app

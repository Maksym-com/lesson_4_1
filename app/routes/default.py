from flask import Blueprint, render_template

bp = Blueprint('default', __name__)

@bp.route("/index")
@bp.route("/")
def index():
    return render_template("base.html")
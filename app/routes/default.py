from flask import Blueprint, render_template
from sqlalchemy import select

from app.models import Job
from app.database import Session

bp = Blueprint('default', __name__)

@bp.route("/index/")
@bp.route("/")
def index():


    return render_template("index.html")

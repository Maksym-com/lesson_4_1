from flask import Blueprint, render_template
from sqlalchemy import select, func

from app.models import Job
from app.database import Session

bp = Blueprint('default', __name__)

@bp.route("/index/")
@bp.route("/")
def index():
    with Session() as session:
        query = select(Job.category).where(func.count(Job.category > 5))
        categories = session.scalars(query).all()


    return render_template("index.html", categories=categories)

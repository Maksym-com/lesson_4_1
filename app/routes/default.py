from flask import Blueprint, render_template
from sqlalchemy import select, func

from app.models import Job, Company
from app.database import Session

bp = Blueprint('default', __name__)

@bp.route("/index/")
@bp.route("/")
def index():
    with Session() as session:
        subquery_categories = (
            select(Job.category, func.count(Job.job_id).label('job_count'))
            .group_by(Job.category)
            .having(func.count(Job.job_id) > 5)
            .alias()
        )

        query_categories = select(subquery_categories.c.category)
        categories = session.scalars(query_categories).all()

        jobs_query = select(Job)
        jobs = session.execute(jobs_query).all()

    return render_template("index.html", categories=categories, jobs=jobs)

@bp.route("get_job")
def get_job():
    return 1123

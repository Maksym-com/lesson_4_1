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

        subquery_companies = (
            select(
                Company.id,
                func.count(Job.job_id).label('job_count')
            )
            .join(Job)
            .group_by(Company.id)
            .order_by(func.count(Job.job_id).desc())
            .limit(50)  # Вибираємо 50 компаній з найбільшою кількістю вакансій
            .offset(15)  # Змініть цей параметр для реалізації посторінкового розподілу
            .alias()
        )

        query_companies = (
            select(
                subquery_companies.c.id,
                Company.img
            )
            .join(Company, subquery_companies.c.id == Company.id)
        )
        companies = session.scalars(query_companies).all()

        jobs_query = select(Job)
        jobs = session.scalars(jobs_query).all()

    return render_template("index.html", categories=categories, jobs=jobs)



import datetime, hashlib

from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import select
from flask_login import login_user, current_user

from app.models import Company, Job
from app.database import Session
from app.forms import RegistrationCompanyForm, LoginCompanyForm, AddJobForm

bp = Blueprint('company', __name__)


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationCompanyForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        remember = form.remember.data
        error = form.password.errors

        if error:
            flash(error)
            return redirect(url_for('company.register'))

        with Session() as session:
            if session.query(Company).filter_by(email=email).first():
                flash(f'Користувач з такою електронною адресою вже зареєстрований. Cпробуйте увійти.')
                return redirect(url_for('company.register'))
            else:
                hashed_password = hash_password(password)
                new_company = Company(name=name, email=email, password=hashed_password, date_joined=datetime.datetime.now())
                session.add(new_company)
                session.commit()
                flash("Ви успішно зарєструвались.")
                login_user(new_company, remember=remember)
                return redirect(url_for('default.index'))

    return render_template("company_reg.html", form=form)


@bp.route('/login', methods=["POST", "GET"])
def login():
    form = LoginCompanyForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        with Session() as session:
            query = select(Company).where(Company.email == email)
            company = session.scalars(query).first()

            if company and company.password == hash_password(password):
                login_user(company, remember=remember)
                flash("Ви успішно увійшли!")
                next_page = request.args.get('next')
                return redirect(next_page or url_for('default.index'))
            elif company:
                flash("Перевірте пароль!")
            else:
                flash("Перевірте електронну адресу!")

    return render_template("company_log.html", form=form)
@bp.route("/add_job", methods=["POST", "GET"])
def add_job():
    form = AddJobForm()
    if current_user.is_authenticated:
        if request.method == "POST" and form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            sphere = form.sphere.data
            category = form.category.data
            requirements = form.requirements.data
            experience = form.experience.data
            location = form.location.data
            salary = form.salary.data
            resume_need = form.resume_need.data
            company_id = current_user.id

            with Session() as session:
                new_job = Job(title=title, description=description, sphere=sphere, category=category,
                              requirements=requirements, experience=experience, location=location, salary=salary,
                              resume_need=resume_need, publication_date=datetime.datetime.now(), company_id=company_id)
                session.add(new_job)
                session.commit()
                flash("Нова вакансія додана!")
                return redirect(url_for("default.index"))

        return render_template("add_job.html", form=form)

    else:
        flash("Спочатку ввійдіть в акаунт!")
        return redirect(url_for("company.login"))





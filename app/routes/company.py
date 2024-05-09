import datetime, hashlib

from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import select
from flask_login import login_user

from app.models import Company
from app.database import Session

from app.forms import RegistrationCompanyForm, LoginCompanyForm

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

            if company:
                hashed_password = hash_password(password)
                if hashed_password == company.password:
                    login_user(company, remember=remember)
                    flash("Ви успішно увійшли!")
                    return redirect(url_for('default.index'))
                else:
                    flash("Перевірте пароль!")
                    return redirect(url_for('company.login'))
            else:
                flash("Перевірте електронну адресу!")
                return redirect(url_for('company.login'))

    return render_template("company_log.html", form=form)



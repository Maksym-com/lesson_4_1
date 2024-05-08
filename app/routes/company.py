import datetime, hashlib

from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import select
from flask_login import login_user

from app.models import Company
from app.database import Session

from app.forms import RegistrationCompanyForm

bp = Blueprint('company', __name__)


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationCompanyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
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
                print(hashed_password)
                new_company = Company(name=name, email=email, password=hashed_password, date_joined=datetime.datetime.now())
                session.add(new_company)
                session.commit()
                flash("Ви успішно зарєструвались.")
                login_user(new_company)
                return redirect(url_for('default.index'))

    return render_template("company_reg.html", form=form)

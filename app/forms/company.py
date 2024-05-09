from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationCompanyForm(FlaskForm):
    name = StringField("Назва компанії", validators=[DataRequired()])
    email = EmailField("Електронна пошта", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(8, 64),
                                                   EqualTo('confirm_password', message="Паролі не збігаються")])
    confirm_password = PasswordField('Повторіть пароль')
    remember = BooleanField('Запам\'ятати мене')
    submit = SubmitField("Зареєструватись")


class LoginCompanyForm(FlaskForm):
    email = EmailField("Електронна пошта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField('Запам\'ятати мене')
    submit = SubmitField("Увійти")

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, EmailField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationUserForm(FlaskForm):
    username = StringField('Логін', validators=[DataRequired(), Length(6, 128)])
    name = StringField("Ім'я", validators=[DataRequired()])
    surname = StringField("Прізвище")
    birth_date = DateField("Дата народження", validators=[DataRequired()])
    email = EmailField("Електронна пошта", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(8, 64),
                                                   EqualTo('confirm_password', message="Паролі не збігаються")])
    confirm_password = PasswordField('Повторіть пароль')
    remember = BooleanField('Запам\'ятати мене')
    submit = SubmitField("Зареєструватись")


class LoginUserForm(FlaskForm):
    login = StringField("Username or email", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    remember = BooleanField('Запам\'ятати мене')
    submit = SubmitField("Log In")

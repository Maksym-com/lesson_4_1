from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField, SelectField, IntegerField
from wtforms.fields.simple import TextAreaField
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


class AddJobForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    description = TextAreaField("Опис")
    requirements = TextAreaField("Вимоги", validators=[DataRequired()])
    category = StringField('Категорія', validators=[DataRequired()])
    experience = SelectField('Досвід',
                             choices=[('Не потібно', "Не потрібно"), ("1 місяць", "1 місяць"), ("3 місяці", "3 місяці"),
                                      ("6  місяців", "6 місяців"), ("1 рік", "1 рік"), ("2+ років", "2+ років")],
                             validators=[DataRequired()])
    sphere = StringField('Сфера', validators=[DataRequired()])
    location = StringField('Розташування', validators=[DataRequired()])
    salary = IntegerField('Плата', validators=[DataRequired()])
    resume_need = BooleanField('Наявність резюме')
    submit = SubmitField("Відіслати вакансію")

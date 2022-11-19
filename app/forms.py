'''
файл хранения классов веб-форм
'''


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Номер полиса', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')

#форма входа для врача
class DocLoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Вход')

# форма регистрации пациента
class RegistrationForm(FlaskForm):
    lastname = StringField('Фамилия', validators=[DataRequired()])
    firstname = StringField('Имя', validators=[DataRequired()])
    patronymic = StringField('Отчество', validators=[DataRequired()])
    day = StringField('День', validators=[DataRequired()])
    year = StringField('Год', validators=[DataRequired()])
    month = StringField('Месяц', validators=[DataRequired()])
    username = StringField('Номер полиса', validators=[DataRequired()])
    password1 = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.get_by_sertificate(username.data)
        if user is not None:
            raise ValidationError('Пожалуйста, введите номер полиса, принадлежащий Вам!')
        return

# форма редактирования профиля
class EditProfileForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Старый пароль', validators=[DataRequired()])
    newpassword1 = PasswordField('Новый пароль', validators=[DataRequired()])
    newpassword1 = PasswordField('Повторите новый пароль', validators=[DataRequired()])
    submit = SubmitField('Изменить информацию о пользователе')


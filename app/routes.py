from app import app
from flask import render_template, flash, redirect
from flask import request
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm, DocLoginForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User



# главная страница
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


# вход для пациента
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect("/index")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_sertificate(form.username.data)
        print("имя найденного пользователя")
        print(user.name)
        #user: User = Users.get_by_sertificate(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect("/login")
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = "/index"
        return redirect(next_page)
    return render_template('client_login.html', title = 'Личный кабинет пациента', form=form)

# вход в систему для врача
@app.route("/doc_login", methods = ['GET', 'POST'])
def doc_login():
    if current_user.is_authenticated:
        return redirect("/index")
    form = DocLoginForm()
    if form.validate_on_submit():
        doctor = Doctor.get_by_login(form.username.data)
        print("имя найденного доктора")
        print(doctor.name)
        # or not doctor.check_password(form.password.data)
        if doctor is None:
            flash('Invalid username or password')
            return redirect("/doc_login")
        login_user(doctor, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = "/index"
        return redirect(next_page)
    return render_template('doc_login.html', title = 'Личный кабинет врача', form=form)


# регистрация в системе для пациента
@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(sertificate = form.username.data,
                name = f'{form.lastname.data} {form.firstname.data} {form.patronymic.data}',
                birthdate =  f'{form.year.data}-{form.month.data}-{form.day.data}')
        user.set_password(form.password1.data)
        user.adduser()
        flash('Вы создали нового пользователя')
        return redirect("/login")
    return render_template('registration.html', title = 'Регистрация в системе', form=form)





# мой профиль
@app.route("/client/<username>", methods = ['GET'])
@login_required
def client(username):
    user = User.get_by_sertificate(username)
    return render_template('client.html', title = 'Личный кабинет пациента', user=user)

# выйти из аккаунта

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/index")

# регистрация пациента
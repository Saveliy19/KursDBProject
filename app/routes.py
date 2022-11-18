from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm, RegistrationForm, DocLoginForm, EditProfileForm
from flask_login import current_user, login_user, logout_user
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
        return redirect("{{ url_for('index') }}")
    form = LoginForm()
    if form.validate_on_submit():
        user: User = Users.get_by_sertificate(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect("{{ url_for('login') }}")
        login_user(user, remember=form.remember_me.data)
        return redirect("{{ url_for('index') }}")
    return render_template('client_login.html', title = 'Личный кабинет пациента', form=form)


# регистрация в системе для пациента
@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(sertificate = form.username.data,
                name = f'{form.lastname.data} {form.firstname.data} {form.patronymic.data}',
                birthdate =  f'{form.year.data}-{form.month.data}-{form.day.data}')
        if form.password1.data != form.password2.data:
            flash('Введенные пароли не совпадают!')
            return render_template('registration.html', title = 'Регистрация в системе', form=form)
        else:
            user.set_password(form.password1.data)
            user.adduser()
            flash('Вы создали нового пользователя')
            return redirect("{{ url_for('login') }}")
    return render_template('registration.html', title = 'Регистрация в системе', form=form)

# вход в систему для врача
@app.route("/doc_login", methods = ['GET', 'POST'])
def doc_login():
    form = DocLoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        return redirect ("/profile")
    return render_template ('doc_login.html', title = 'Личный кабинет врача', form=form)

# редактирование собственного профиля
@app.route("/edit_profile", methods = ['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        return redirect ("{{ url_for('index') }}")
    return render_template('edit_profile.html', title='Редактировать профиль', form=form)


# мой профиль
@app.route("/profile", methods = ['GET'])
def profile():
    return render_template('profiles.html', title = 'Редактировать профиль')

# выйти из аккаунта
@app.route("/logout")
def logout():
    logout_user()
    return redirect("{{ url_for('index') }}")

# регистрация пациента
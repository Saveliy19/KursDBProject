from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm, RegistrationForm




@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect("{{ url_for('index') }}")
    return render_template('login.html', title = 'Вход', form=form)

@app.route("/registration", methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.name.data))
        return redirect("{{ url_for('login') }}")
    return render_template('registration.html', title = 'Регистрация в системе', form=form)
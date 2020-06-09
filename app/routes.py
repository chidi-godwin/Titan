from app import app, db
from app.forms import SignupForm, LoginForm
from app.models import User, Transaction
from flask import render_template, redirect, url_for, request, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, 
                    first_name=form.first_name.data, last_name=form.last_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You've been sucessfully registered!")          
        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() or \
            User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('signin'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('welcome')
        return redirect(next_page)
    return render_template('signin.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/print')
@login_required
def print():
    return render_template('print.html')

@app.route('/records')
@login_required
def records():
    return render_template('table.html')
from app import app, db
from app.forms import SignupForm, LoginForm, DateForm
from app.models import User, Transaction, Role
from flask import render_template, redirect, url_for, request, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = SignupForm(request.form)
    if form.validate_on_submit():
        print(form)
        user = User(username=form.username.data, email=form.email.data, 
                    first_name=form.first_name.data, last_name=form.last_name.data, 
                    role=Role.query.filter_by(role='Teller').first()) 
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
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() or \
            User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('signin'))
        login_user(user, remember=False)
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
def printer():
    return render_template('print.html')

@app.route('/records', methods=['GET', 'POST'])
@login_required
def records():
    form = DateForm(request.form)
    if form.validate_on_submit:
        records = Transaction.query.filter(Transaction.date.between(form.fromm.data, form.to.data))
        return render_template('report.html', records=records)
    records = Transaction.query.all()
    return render_template('report.html', records=records, form=form)

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/token')
@login_required
def token():
    return render_template('token.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/manager')
def manager():
    return render_template('manager.html')
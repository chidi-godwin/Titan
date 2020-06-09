from app import app
from app.forms import SignupForm, LoginForm
from flask import render_template, redirect, url_for, request

app.config['SECRET_KEY']='KNOWYOURWORTH'
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    form_data = request.data
    if form.validate_on_submit():
        return redirect(url_for('welcome'))
    return render_template('signin.html', form=form)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/print')
def print():
    return render_template('print.html')

@app.route('/records')
def records():
    return render_template('table.html')
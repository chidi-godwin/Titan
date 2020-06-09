from app import app
from app.forms import SignupForm, LoginForm
from flask import render_template, request

app.config['SECRET_KEY']='KNOWYOURWORTH'
@app.route('/', methods=['GET', 'POST'])
def index():
    return "hello World"

@app.route('/signup', methods=['GET', 'POSTS'])
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POSTS'])
def signin():
    form = LoginForm()
    return render_template('signin.html', form=form)
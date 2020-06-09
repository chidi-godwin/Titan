from app import app
from app.forms import SignupForm
from flask import render_template, request

app.config['SECRET_KEY']='KNOWYOURWORTH'
@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form
    print(data)
    return render_template('signup.html')

@app.route('/index', methods=['GET', 'POSTS'])
def index2():
    form = SignupForm()
    return render_template('flask_sign.html', form=form)
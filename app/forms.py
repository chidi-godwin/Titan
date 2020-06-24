from app.models import User
from flask_wtf import FlaskForm
from flask import Markup
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from datetime import datetime


class SignupForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    phone = StringField('phone', validators=[DataRequired(), Length(min=11)])
    role = SelectField('role', choices=[("Teller", "Teller"), ("Manager", "Manager")])
    confirm_email = StringField('comfirm email', validators=[
                                DataRequired(), Email(), EqualTo('email')])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address has been used')

    def validate_password(self, password):
        if not all([any(char.isdigit() for char in password.data), any(char.islower()\
             for char in password.data), any(char.isupper() for char in password.data)]):
                 raise ValidationError('passwords must contain at least one lowercase, uppercase and digit')
    def validate_phone(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user is not None:
            raise ValidationError("This number had been used")

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class DateForm(FlaskForm):
    fromm = DateField('fromm')
    to = DateField('to')

class BranchForm(FlaskForm):
    branch = StringField('branch')
    manager = StringField('manager')

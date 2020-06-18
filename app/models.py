from app import db, login
from datetime import datetime, date, time
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    transactions = db.relationship(
        'Transaction', backref='officer', lazy='dynamic')
    managers = db.relationship(
        'Manager', backref='officer', lazy='dynamic')
    tellers = db.relationship(
        'Teller', backref='officer', lazy='dynamic')
    admins = db.relationship(
        'Admin', backref='officer', lazy='dynamic')
    

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.String(64), nullable=False, unique=True)
    account_name = db.Column(db.String(64), nullable=False)
    account_number = db.Column(db.String(11), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    commission = db.Column(db.Float, nullable=False, default=650.34)
    vat = db.Column(db.Float, nullable=False, default=123.67)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    trans_details = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today())
    time = db.Column(db.Time, nullable=False, default=time(
        datetime.now().hour, datetime.now().minute))

    def __repr__(self):
        return f"<Transaction {self.ref_id}>"

    @hybrid_property
    def total_debit(self):
        return self.amount + self.commission + self.vat


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64), nullable=False, unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f"<Role {self.role}>"

class Teller(db.Model):
    __tablename__='tellers'
    id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('managers.id'))
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Teller {self.officer.username}>"


class Manager(db.Model):
    __tablename__ = 'managers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
    tellers = db.relationship('Teller', backref='manager', lazy='dynamic')

    def __repr__(self):
        return f"<Manager {self.officer.username}>"

class Branch(db.Model):
    __tablename__ = 'branches'
    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(255), nullable=False, unique=True)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    managers = db.relationship('Manager', backref='branch', lazy='dynamic')

    def __repr__(self):
        return f"<Branch {self.branch}>"

class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(255), nullable=False, unique=True)
    branches = db.relationship('Branch', backref='region', lazy='dynamic')
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))

    def __repr__(self):
        return f"<Region {self.region}>"

class Admin(db.Model):
    __tablename__='admins'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    regions = db.relationship('Region', backref='admin', lazy='dynamic')
    
    def __repr__(self):
        return f"<Admin {self.officer.username}>"

@login.user_loader
def load_user(username):
    return User.query.get(username)

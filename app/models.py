from app import db, login
from datetime import datetime
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
    transactions = db.relationship('Transaction', backref='officer', lazy='dynamic')

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.String(64), nullable=False, unique=True, index=True)
    account_name = db.Column(db.String(64), nullable=False)
    account_number = db.Column(db.String(11), nullable=False)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    commission = db.Column(db.Float, nullable=False, default=650.34)
    vat = db.Column(db.Float, nullable=False, default=123.67)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    trans_details = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Transaction {self.ref_id}>"

    @hybrid_property
    def total_debit(self):
        return self.amount + self.commission + self.vat

@login.user_loader
def load_user(username):
    return User.query.get(username)
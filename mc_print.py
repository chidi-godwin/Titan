from app import app, db
from app.models import User, Transaction, Role, Teller, Manager, Branch, Region, Admin
from flask import session
from datetime import timedelta


@app.shell_context_processor
def make_shell_context():
    return {
            'db': db, 
            'User': User, 
            'Transaction': Transaction, 
            'Role': Role, 
            'Admin':Admin, 
            'Region':Region, 
            'Branch':Branch, 
            'Manager':Manager, 
            'Teller':Teller
            }

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)
    session.modified = True
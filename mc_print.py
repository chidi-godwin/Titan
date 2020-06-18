from app import app, db
from app.models import User, Transaction, Role, Teller, Manager, Branch, Region, Admin


@app.shell_context_processor
def make_shell_context():
    return {
            'db': db, 
            'User': User, 
            'Transaction': Transaction, 
            'Role': Role, Admin:'Admin', 
            'Region':Region, 
            'Branch':Branch, 
            'Manager':Manager, 
            'Teller':Teller
            }
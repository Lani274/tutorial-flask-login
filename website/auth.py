from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up </p>"
# log in, log out and sign in Navigierung mit / nach der URL Tetx wird ausgegeben
# how to set up the routes and URls in flask
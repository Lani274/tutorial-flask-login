from flask import Blueprint, render_template

# es hat viele routes das bedeutet Blueprint

views = Blueprint('views', __name__)

@views.route('/') #decorator
def home(): 
    return render_template("home.html")


# this function will always run whenever we go into our url and type / we will go to
# our main page of our website, whatever is inside of home will run 
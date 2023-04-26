# Tutorial Flask-Login
Tutorial Flask-Login in the course "316002 Entwicklung von Web-Anwendungen" 

Professor: Prof. Dr. Alexander Eck

Winter Term 2022/23

Submitted by Lana Aram 

---

### *Disclaimer*

This tutorial draws heavily from [this video](https://www.youtube.com/watch?v=dam0GPOAvVI&t=4255s). The code for the web app has been mostly copied from this tutorial.

I tested the code on my current Windows 11 machine and I will show in this tutorial how it works on Windows, not on macOS, therefore I don't guarantee that it will work as described on a Mac. If you have a Mac you might need to research further sources.

---

## Table of Contents
---

1. [Learning Objectives](#learning-objectives)
2. [Assumptions](#assumptions)
3. [Setup](#setup)
4. [Hello, World!](#hello)
5. [Create the base for the Web App](#concept)
    - [Create a Flask App ](#concept1)
    - [Create Routes/ Views](#concept2)
    - [Jinja Templating Language & HTML Templates](#concept3)
6. [Flask-Login](#concept)
    - [Database Models ](#concept1)
    - [Creating New User Accounts](#concept2)
    - [Adding the Login Method](#concept3)

7. [Follow-Ups & Sources](#sources)

---
## 1. Learning Objective  
---

The Learning Objectives are firstly to set up Python and Visual Studio Code. Then to create a running  Flask application that demonstrates and visualizes how Flask-Login can be used. By the end of this tutorial, you should have a website, mostly written with Python, where a user can login and logout. Therefore, the user needs an account which is stored in a database. In addition, the user can save notes in a list and only the notes of the logged in user are displayed. The goal is that you will not only understand Flask-Login, but also know how basic-mechanisms of Python are used. Come back here as often as you need, it serves as a beginner tutorial which can be implemented in  more web apps. Through this happy path you will understand how Flask-Login can be implemented into a web app. So, let's dive in!

To-Do:
- [ ] Setting up Python and Visual Studio Code
- [ ] Launching a web server
- [ ] Create a user account
- [ ] Store this data in a database
- [ ] Login into the user account and logout 
- [ ] Associate notes with a specific user

---
## 2. Assumptions
---

I assume that you don't have Visual Studio Code installed on your computer and start from scratch. You don't need any prior knowledge about Flask-Login. But it is beneficial if you have some knowledge about Python or Java, or in general programming languages that support object-oriented programming. I also assume that you have a basic understanding of HTML and CSS.  

It's best if you code while you read the tutorial, therefore you will implement a happy path while you are discovering new knowledge about Flask-Login.

### What's in Scope (3b):

- Flask built-in 


### What's out of Scope:

- 

---
## 3. Setup
---
The setup for your development environment will mostly follow [this tutorial](https://code.visualstudio.com/docs/python/python-tutorial) and also the notebook "03d - How to set up Python and VS Code" from the class "316002 Entwicklung von Web-Anwendungen" by Prof. Dr. Alexander Eck. 

By completing this setup you will have all the prerequisites to further follow the Flask-Login Tutorial. 

### **Install Python**
- Download and install Python from [python.org](https://www.python.org/downloads/) and activate the checkbox of the "Use admin privileges when installin py.exe".


### **Create a project folder with a Python Virtual Environment**
#### **Create a project folder**
You need to create a new folder    */webapp*. Your full path on Windows might then look like *C:\Users\me\projects\webapp*

#### **Create a Python Virtual Environment and install Flask**
It is very likely that you now have your Explorer window open in the */webapp* folder. If you have German Windows press Alt+D. Next, press P. It will open the Windows terminal application that is called "PowerShell". 

With your terminal window open, type:
````
python -m venv .venv
````

The .venv folder has been now created, but now we need to activate this particular Python Virtual Environment:
````
.\.venv\Scripts\Activate.ps1
````
If you get an error, run the following line and then try the command for the acitvation again:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
You will see that the PowerShell row will begin with *(.venv)* which shows that the Python Virtual Environment has been activated. From here, you can now install Flask with this command:
```bash
pip install flask
```
### **Installation of Visual Studio Code and Activation of the Python Virtual Environment**

#### **Install Visual Studio Code with the Python extension**

Download and install Visual Studio Code from [this link](https://code.visualstudio.com/) . 

Start the program and then press *Shift + Ctrl + X* to open the "Marketplace Extensions". Search for the Python extension from Microsoft and install it. Lastly, check on the extension's page, if the extension has been enabled. 

#### **Create an active workspace with your project folder**

Press *Ctrl+K+0* and navigate to your */webapp* folder. Set it as the folder of the IDE (integrated development environment, i.e. Visual Studio Code).

On the side pane your should now see the */.venv* folder that was cretaed before. In the */Lib* folder you should see flask, if not is has not been installed correctly. 

### **Activate the Python Virtual Environment of your project**

Press *Shift+Ctrl+P* to open the command pallete and type *python select interpreter*. Accept the command and press *Enter*. Choose the Python interpreter from the */.venv/Scripts* folder. This will be the Python Virtual Environment of your project. 

Then press *Shift+Ctrl+P* and start typing *terminal create new terminal*. Press *Enter* and a new terminal window should open in the lower part of your Environment. There the row should begin with *(.venv)*. 

You may also want to create a GitHub repository and document your progress using commits. Here are some recommendations and helpful resources to get familiar with [Git & GitHub](https://docs.github.com/en/get-started/quickstart). 

You may also have questions which can be answered using [StackOverflow](https://stackoverflow.com/questions). 

Everything has been set up, we have all the requirements and we are ready to code our 'Hello, World!' with Python!. 

What we have done:
- [ ] We installed Python and Visual Studio Code
- [ ] We created a project folder
- [ ] We installed Flask within a Python Virtual Environment in your project folder

---
## 4. Hello, World! 
---
Assuming that you have done the Setup, press *Shift+Ctrl+P* and type *file new file*. Accept the command with *Enter* and your side pane should open. Name the file *app.py* and type in this Python code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
return 'Hello, World!'
```
This example was taken from the notebook "03b - Full stack web dev intro notebook" from the class "316002 Entwicklung von Web-Anwendungen" by Prof. Dr. Alexander Eck.

This minimal Flask application launches the webserver. The result is a Flask-powered "Hello, World!" web app.

*What you see in the code:* 
*@app.route()* is a Python decorator. Decorators take functions, extend them and return, so that a function can basically return a function (vgl. Python Decorators Introduction - Python Tutorial n.d.). The most common use in Flask is to specify the URL route with that. Every route is a certain page in the web app. 

Save the changes with *Ctrl+S*. Click into your terminal and type 

```bash
flask run 
```
The Flask built-in development web server should show up. Now hold down *Ctrl* and *left-click* on the URL *127.0.0.1:5000*. It should open your standard browser at that URL with a *Hello, World!* message. 

Inside the terminal type *pip install flask-login*. 
After the installtion also type *pip install flask-sqlalchemy*. 
We need these modules to use Flask-Login and Flask-Sqlalchemy to later create database models. 

----
## 5. Create the base for the Web App 
-----

Now that we have all the prerequisites we can begin with the actual web-app. With Flask-Login we have a Flask extension that allows to use user authentication functionality (vgl. Flask-Login — Flask-Login 0.7.0 documentation n.d.). 

Firstly, we need to strucuture our directory structure. Delete the *app.py* file from the Hello, World example if you have done it. Inside our  */webapp* folder create new folders and files with this strucutre. Therefore your project folder */webapp* might look like this.

* [static/](./website/static)
  * [index.js](./website/static/index.js)
* [templates/](./website/templates)
  * [base.html](./website/templates/base.html)
  * [home.html](./website/templates/home.html)
  * [login.html](./website/templates/login.html)
  * [sign_up.html](./website/templates/sign_up.html)
* [auth.py](./website/auth.py)
* [models.py](./website/models.py)
* [views.py](./website/views.py)
* [__ init__.py](./website/__init__.py)

Outside the */webapp* folder we need the file **main.py**, which is not shown above as it only shows the */webapp* folder. 

----
### 5.1 Create a Flask App
-----

Inside the *__ init__.py* extend with the following code:

```python
from flask import Flask

def create_app(): #define function create_app()
    app = Flask(__name__) #initialize the app
    app.config['SECRET_KEY'] = 'dsjkajeijw' #encrypt the session data related to our web-app
    
    return app
```
We created the flask app and defined the function create_app() which returns the app.

Go to *main.py*.

```python
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

We now import our website package, or what might be called webapp in your case, and grab that create_app function from  the *__ init__.py* file and use that to actually create an application which can be run. 
*if __ name__ == '__ main__':* etc.
states that I only want to run the web server if we run the *main.py* file. app.run(debug=True) means that everytime we will make a change in our Python code, it will automatically run the webserver (vgl. How to debug a Flask app n.d.). 


----
### 5.2 Create Routes/ Views 
-----

Go into the *views.py* file. There we will create our routes so that our user can navigate through different pages in our web app. Extend with the following code. 

```python
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home(): # this function will run whenever we go to the slash route (our main page)

```
We created a Blueprint object called views and we can now add views to the Blueprint object using the route decorator. If you want to know more about using Blueprint [read more on this page](https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like).

Do the same thing in *auth.py* but change the Blueprint object into *auth*. 

```python
from flask import Blueprint

auth = Blueprint('auth', __name__)
```

Inside the *__ init__.py* file 
we need to tell this file that we have blueprints containing different views for our application. 

Your *__ init__.py* file  should now look like this: 
```python
from flask import Flask

def create_app(): 
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'dsjkajeijw'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
```
We are now basically importing the Blueprint object from *views.py* which is called views and also from *auth.py* which is called auth. Then we need to register them into our flask application with register_blueprint(). When a Flask Blueprint is registered, the application is extended with its contents (vgl. Python 2021). 

Back to our *auth.py* file extend with this code: 

```python
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route(/login)
def login():
    return "<p>Login</p>"

@auth.route(/logout)
def logout():
    return "<p>Logout</p>"

@auth.route(/sign-up)
def sign_up():
    return "<p>Sign Up</p>"
```

You can now run your webserver by going to your main.py file and clicking on the run button on the right-hand corner. What the above code is intented to do, is to create a navigation for the user through our web app. If you go to the URL bar, in your opened up standard browser, at the top and change the last "/" to "/sign-up", it will go to our Signup page for our user. It will also show the output of the sign_up() function in your browser. You can also do that with "/login" and "/logout".This mechanism is called Routing (vgl. Python - Routing n.d.).  

---
### 5.3 Jinja Templating Language & HTML Templates
---

Jinja2 is a python HTML template engine, which means that HTML documents will be combined with data. It is installed with Flask. Jinja2 offers many options for formatting data in the HTML file (vgl. Admin 2021). Inside our template folder we created a base.html file, which is the base templated and creates the theme of the web app. The other files in the templates folder will then override parts of the base.html with more specific parts (vgl. Admin 2021). 

Extend *base.html* with this code (it is best to copy it):

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
            />
        <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      crossorigin="anonymous"
            />        
        <title>{% block title %}Home{% endblock %}</title>
    </head>
</html>
```
I will not dive deep into HTML and CSS stylesheets as this is not part of this tutorial. However, we imported bootstrap into the code, which is a CSS framework which allows to use pre-build classes for our website design (vgl. Contributors n.d.). The links allow to load custom CSS content and classes, without downloading a specific file. We can then use them into our HTML file. Inside the *{%%}* (called Delimiters) you can actually write Python code, like if statements (vgl. Basic Syntax of Jinja n.d.). With *block title* we create the Home title of our page, which then can be overriden in another template e.g. Login, where the title needs to be changed (vgl. Jinja2 Default Page Title n.d.).  


Under the end head tag continue with this code, which are JavaScript scripts, inside the body tags: 
```html
    <body>
        <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>

    <script>
      type="text/javascript"
      src="{{ url_for('static', filename='index.js')}}"
    </script>
    </body>
</html>
```
Above the script tags, but inside the body tags, continue with extending this code:
```html

      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar">
              <span class="navbar-toggler-icon"></span>
          </button>
        <div class="collapse navbar-collapse" id="navbar">
          <div class="navbar-nav">
            {% if user.is_authenticated %}
            <a class="nav-item nav-link" id="home" href="/">Home</a>
            <a class="nav-item nav-link" id="logout" href="/logout">Logout</a>
            {% else %}
            <a class="nav-item nav-link" id="login" href="/login">Login</a>
            <a class="nav-item nav-link" id="signUp" href="/sign-up">Sign Up</a>
            {% endif %}
          </div>
        </div>
      </nav>
```
This code will create a navigation bar which links to the different pages. 
Underneath the end nav tag continue with this code:
```html
      <div class="container">
        {% block content %}
        {% endblock %}
      </div>
```

Go to *home.html*, where we will extend the *base.html* template witht he following code. *home.html* can now override *base.html* (vgl. Template Inheritance — Jinja Documentation n.d.). 

!!!!!!!!!!!!!!!!!!!!!
```html
{% extends "base.html" %} {% block title %}Home{% endblock %}

{% block content %}
<h1>This is the home page</h1>
{% endblock %}
```


Inside the *views.py* file add this code, so that the *home.html* template will be returned.

```python
from flask import Blueprint
,render template #add this code

views = Blueprint('views', __name__)

@views.route('/')
def home(): 
    return render_template("home.html") # add this code
```


We will now look at the *login.html* and *sign_up.html* file. Go into *login.html* and add this code:

````html
{% extends "base.html" %} {% block title %}Login{% endblock %}

{% block content %}
<h1>This is the login page</h1>
{% endblock %}
````


Go to *sign_up.html* and add the similar code.

````html
{% extends "base.html" %} {% block title %}Sign Up{% endblock %}

{% block content %}
<h1>This is the sign up page</h1>
{% endblock %}
````


Inside of *auth.py* we don't want the html code inside, but instead our templates. Replace the *p* tags with render_template().
Also add the code shown in the comments:
```python
from flask import Blueprint, render_template # add this

auth = Blueprint('auth', __name__)

@auth.route(/login)
def login():
    return render_template("login.html") # replace p tag with this code

@auth.route(/logout)
def logout():
    return "<p>Logout</p>"

@auth.route(/sign-up)
def sign_up():
    return render_template("sign_up.html") # replace p tag with this code
```

Go to *sign_up.html* and replace the *h1* tags with this code.

````html
{% extends "base.html" %} {% block title %}Sign Up{% endblock %}

{% block content %}
<form method="POST">
    <h3 align="center">Sign Up</h3>
    <div class="form-group">
        <label for="email">Email Adress</label>
        <input type="email" class="form-control" id="email" name="email" placeholder="Enter email"/>
    </div>
    <div class="form-group">
        <label for="firstName">First Name</label>
        <input type="text" class="form-control" id="firstName" name="firstName" placeholder="Enter first name"/>
    </div>
    <div class="form-group">
        <label for="password1">Password</label>
        <input type="password" class="form-control" id="password1" name="password1" placeholder="Enter password"/>
    </div>
    <div class="form-group">
        <label for="password2">Password (Confirm)</label>
        <input type="password" class="form-control" id="password2" name="password2" placeholder="Confirm password"/>
    </div>
    <br />
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
{% endblock %}
````
This code will create four labels for our sign up page and also four fields to let the user enter his email, first name and password. We will also have a submit button. 

Now go to *login.html* and replace the h1 tag with the following code:

````html
{% extends "base.html" %} {% block title %}Login{% endblock %}

{% block content %}
<form method="POST">
    <h3 align="center">Login</h3>
    <div class="form-group">
        <label for="email">Email Adress</label>
        <input type="email" class="form-control" id="email" name="email" placeholder="Enter email"/>
    </div>
    <div class="form-group">
        <label for="password">Password</label>
        <input type="password" class="form-control" id="password" name="password" placeholder="Enter password"/>
    </div>
    
    <br />
    <button type="submit" class="btn btn-primary">Login</button>
</form>
{% endblock %}
````
With this code the user now can see fields for his email and password, but also a submit button. 
Moreover, the POST-method is a HTTP request, which allows to send the information, put in by the user into the fields, to our server. We do that by clicking on the submit button. If you want to know more about HTTP requests look [here](https://www.ionos.de/digitalguide/hosting/hosting-technik/http-request-erklaert/). 

Inside of *auth.py* we want to now handle these post requests. Extend your code:

```python
from flask import Blueprint, render_template, request, flash # add this

auth = Blueprint('auth', __name__)

@auth.route(/login, methods=['GET', 'POST']) # add code
def login():
    return render_template("login.html") 

@auth.route(/logout)
def logout():
    return "<p>Logout</p>"

@auth.route(/sign-up, methods=['GET', 'POST'])# add code
def sign_up():# add following code
         if request.method == 'POST':
         email = request.form.get('email')
         first_name = request.form.get('firstName')
         password1 = request.form.get('password1')
         password2 = request.form.get('password2')

if user:
             flash('Email already exists.', category='error')

         elif len(email) < 4:
             flash('Email must be greater than 3 characters.', category='error')
         elif len(first_name) < 2:
             flash('First name must be greater than 1 character.', category='error')
         elif password1 != password2:
             flash('Passwords dont match.', category='error')
         elif len(password1) < 7:
             flash('Password must be at least 7 characters.', category='error')
    return render_template("sign_up.html") 
```
What we do now is to check, if the information submitted by the user is correct, but we also want to warn or alert them with Message Flashing, if something goes wrong. We need to import flash and use the flash() function. We categorize them into error, so that the messages have a red color. For more information on Message Flashing with Flask look [here](https://flask.palletsprojects.com/en/2.0.x/patterns/flashing/). 

For that, go to the *base.html* file and write this code under the nav end tag.

````html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
     {% for category, message in messages %}
     {% if category == 'error' %}
     <div class="alert alert-danger alter-dismissable fade show" role="alert">
      {{ message }}
      <button type="button" class="close" data-dismiss="alert">
        <span aria-hidden="true">&times;</span>
      </button>
     </div>
     {% else %}
     <div class="alert alert-success alter-dismissable fade show" role="alert">
      {{ message }}
      <button type="button" class="close" data-dismiss="alert">
        <span aria-hidden="true">&times;</span>
      </button>
     </div>
     {% endif%}
     {% endfor %}
    {% endif %}
    {% endwith %}
````
We now can message the user, if something went wrong. 

---
## 6. Flask-Login 
---
---
### 6.1 Database Models
---

Go into your *__ init__.py* file and add the following code: 

````python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy #add

db = SQLAlchemy() #add the following code
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'dsjkajeijw' # add the following code
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
````
Our database name is now called *database.db* and we have the database object called db. With db.init_app(app) we will take the database object and link it to our flask app (vgl. Tech With Tim 2021b). 

Inside our *models.py* file we will create our database models. We want to have two database models, one for our users and one for our notes. 
````python
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin): #uses UserMixin
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
````
Firstly, we imported our db object that we created before. We will also import UserMixin from the flask_login module. This User Object Helper provide defaul implementations for the methods that Flask-Login expects user objects to have (vgl. Flask-Login — Flask-Login 0.7.0 documentation n.d.). You can see that the User class uses UserMixin. The question now is why. Flask-Login requires a User model to have the following properties (vgl. What is the UserMixin in Flask? n.d.):

- has an is_authenticated() method that returns True if the user has provided valid credentials
- has an is_active() method that returns True if the user’s account is active
- has an is_anonymous() method that returns True if the current user is an anonymous user
- has a get_id() method which, given a User instance, returns the unique ID for that object

What the UserMixin class is now doing is that it provides the implementation of these properties. For example, the function is_authenticated() can be used instaed of writing an own method (vgl. What is the UserMixin in Flask? n.d.).

The User class will have 5 columns id, email, password, first_name and notes. With unique=True it means that no user can have the same email as another user. We also want to know which user created which note. Therefore, we also have a column that refers to the note id from the Note table.   

## User
| *id* | email | password | first_name | notes |
|----|-------|----------|------------|-------|
| 1   |   x@x.de    |   123       |      Max     |   1    |

The Note class will have id, data, date an user_id as columns. All of the notes need to be associated to a specific user, therefore we need a foreign key relationship that specifically references a column from one table to the other table. Therefore, for every note, we want to know to whom it belongs. For that we have the column user_id, which links to an existing user from the the User class. Therefore, one user can have many notes. 

## Note
| *id* | data | date | user_id| 
|----|-------|----------|------------|
|   1 |   xxx    |xx.xx.xxx          |   1         |       

We always need a primary key e.g. an id as an Integer, because the two users can have the same name but not the same id. 

Now that we defined our database models, we want to actually create them. For that we want to check everytime, if the database have been created yet. Go into your *__ init__.py* file and add the following code. Then run it:  

````python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path #add

db = SQLAlchemy() 
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'dsjkajeijw' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note #add
    
    return app

def create_database(app): # add
    if not path.exists('webapp/' +  DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
````
Firstly, we imported the models we created: User and Note. With the function create_database() we now created a database.db file that most likely is located in the instance folder of your webapp. 

---
### 6.2 Creating New User Accounts
---

Now go to your *auth.py* file:

```python
from flask import Blueprint, render_template, request, flash, redirect, url_for # add
from .models import User # add the following code
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route(/login, methods=['GET', 'POST']) 
def login():
    return render_template("login.html") 

@auth.route(/logout)
def logout():
    return "<p>Logout</p>"

@auth.route(/sign-up, methods=['GET', 'POST'])
def sign_up():
         if request.method == 'POST':
         email = request.form.get('email')
         first_name = request.form.get('firstName')
         password1 = request.form.get('password1')
         password2 = request.form.get('password2')
# if this return  a user, the email already exist
         user= User.query.filter_by(email=email).first()

         if user:
             flash('Email already exists.', category='error')

         elif len(email) < 4:
             flash('Email must be greater than 3 characters.', category='error')
         elif len(first_name) < 2:
             flash('First name must be greater than 1 character.', category='error')
         elif password1 != password2:
             flash('Passwords dont match.', category='error')
         elif len(password1) < 7:
             flash('Password must be at least 7 characters.', category='error')
         else: # add
            # create a new user and hash the password
             new_user= User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
             # add the new user to the database
             db.session.add(new_user)
             db.session.commit()
             login_user(user, remember=True)
             flash('Account created!', category='success')
             return redirect(url_for('views.home')) # if user is found, it gets redirected back to the home page, we map which function links to the url
 
     return render_template("sign_up.html", user=current_user) 
```
Here we check if the data that the user submitted to the form is correct, if valid then we add it to the database. We also need to make sure that the password is getting hashed before putting the data into the database, because it is important to remember, that storing passwords in plain text is considered a poor security practice (vgl. Herbert 2021).  

---
### 6.3 Adding the Login Method
---

Now go to your *auth.py* file:

```python
from flask import Blueprint, render_template, request, flash, redirect, url_for # add
from .models import User # add the following code
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route(/login, methods=['GET', 'POST']) 
def login():
    return render_template("login.html") 

@auth.route(/logout)
def logout():
    return "<p>Logout</p>"

@auth.route(/sign-up, methods=['GET', 'POST'])
def sign_up():
         if request.method == 'POST':
         email = request.form.get('email')
         first_name = request.form.get('firstName')
         password1 = request.form.get('password1')
         password2 = request.form.get('password2')
# if this return  a user, the email already exist
         user= User.query.filter_by(email=email).first()

         if user:
             flash('Email already exists.', category='error')

         elif len(email) < 4:
             flash('Email must be greater than 3 characters.', category='error')
         elif len(first_name) < 2:
             flash('First name must be greater than 1 character.', category='error')
         elif password1 != password2:
             flash('Passwords dont match.', category='error')
         elif len(password1) < 7:
             flash('Password must be at least 7 characters.', category='error')
         else: # add
            # create a new user and hash the password
             new_user= User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
             # add the new user to the database
             db.session.add(new_user)
             db.session.commit()
             login_user(user, remember=True)
             flash('Account created!', category='success')
             return redirect(url_for('views.home')) # if user is found, it gets redirected back to the home page, we map which function links to the url
 
     return render_template("sign_up.html", user=current_user) 
```












---
## Sources
---
- https://code.visualstudio.com/docs/python/python-tutorial
- Tech With Tim (2021b): Python Website Full Tutorial - Flask, Authentication, Databases & More, [YouTube] https://www.youtube.com/watch?v=dam0GPOAvVI.
- notebook "03d - How to set up Python and VS Code" from the class "316002 Entwicklung von Web-Anwendungen" of Prof. Dr. Alexander Eck. 
- the notebook "03b - Full stack web dev intro notebook" from the class "316002 Entwicklung von Web-Anwendungen" by Prof. Dr. Alexander Eck.
- https://pythonbasics.org/decorators/
- Flask-Login — Flask-Login 0.7.0 documentation (n.d.): [online] https://flask-login.readthedocs.io/en/latest/.
- How to debug a Flask app (n.d.): Stack Overflow, [online] https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app.
- Python, Real (2021): Use a Flask Blueprint to Architect Your Applications, in: realpython.com, [online] https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like.
- Python - Routing (n.d.): [online] https://www.tutorialspoint.com/python_network_programming/python_routing.htm.
- Admin (2021): Flask Templates with Jinja2 Explained in Detail | GoLinuxCloud, in: GoLinuxCloud, [online] https://www.golinuxcloud.com/flask-template/.
- Contributors, Mark Otto Jacob Thornton, and Bootstrap (n.d.): Introduction, [online] https://getbootstrap.com/docs/5.0/getting-started/introduction/.
- Basic Syntax of Jinja (n.d.): Engagement, [online] https://documentation.bloomreach.com/engagement/docs/jinja-syntax.
- Jinja2 Default Page Title (n.d.): Stack Overflow, [online] https://stackoverflow.com/questions/12339324/jinja2-default-page-title#:~:text=Use%20a%20block%3A%20%3Ctitle%3E%20%7B%25%20block%20title%20%25%7D,template%20if%20you%20want%20to%20change%20the%20title.
-Template Inheritance — Jinja Documentation (n.d.): [online] https://svn.python.org/projects/external/Jinja-1.1/docs/build/inheritance.html.
- Der HTTP-Request einfach erklärt (2020): IONOS Digital Guide, [online] https://www.ionos.de/digitalguide/hosting/hosting-technik/http-request-erklaert/.
- Flask-Login — Flask-Login 0.7.0 documentation (n.d.): [online] https://flask-login.readthedocs.io/en/latest/#how-it-works.
- What is the UserMixin in Flask? (n.d.): Stack Overflow, [online] https://stackoverflow.com/questions/63231163/what-is-the-usermixin-in-flask.
- Herbert, Anthony (2021): How To Add Authentication to Your App with Flask-Login, in: DigitalOcean, [online] https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login.

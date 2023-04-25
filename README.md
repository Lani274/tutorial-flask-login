# Tutorial Flask-Login
Tutorial Flask-Login in the course "316002 Entwicklung von Web-Anwendungen" 

Professor: Prof. Dr. Alexander Eck

Winter Term 2022/23

Submitted by Lana Aram 

---

### *Disclaimer*

This tutorial draws heavily from [this video](https://www.youtube.com/watch?v=dam0GPOAvVI&t=4255s). The code for the web-app has been mostly copied from here.

I tested the code on my current Windows 11 machine and show how it works on Windows, not on macOS, therefore I don't guarantee that it will work as described on a Mac. If you have a Mac you might need to research further sources.

---

## Table of Contents
---
1. [Learning Objectives](#learning-objectives)
2. [Assumptions](#assumptions)
3. [Setup](#setup)
4. [Hello, World!](#hello)
5. [Concept](#concept)
5.1 [What is Flask](#concept)
6. [Follow-Ups & Sources](#sources)

---
## 1. Learning Objective  
---

The Learning Objectives are firstly to set up Python and Visual Studio Code. Then to create a running  Flask application that demonstrates and visualizes how Flask-Login can be used. By the end of this tutorial you should have a website, mostly written with Python, where a user can login and logout. Therefore, the user needs an account. In addition, the user can save notes in a list and only the notes of the logged in user are displayed. Come back here as often as you need, it serves as a beginner tutorial. Through this happy path you will understand how Flask-Login can be implemented. So let's dive in!

To-Do:
- [ ] Setting up Python and Visual Studio Code
- [ ] Create a User Account
- [ ] Store this data in a database
- [ ] Login into the User Account and Logout 
- [ ] Associate notes with a specific user

---
## 2. Assumptions
---

I assume that you don't have Visual Studio Code installed on your computer and start from scratch. You don't need any prior knowledge about Flask-Login. But it is beneficial if you have some knowledge about Python or Java, or in general programming languages that support object-oriented programming.  

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
It is very likely that you now have your Explorer window open in the */webapp* folder. If you have German Windows press from there Alt+D. Next, press P. It will open the Windows terminal application that is called "PowerShell". 

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
*@app.route()* is a Python decorator. Decorators take functions, extend them and return, so that a function can basically return a function (vgl. Python Decorators Introduction - Python Tutorial n.d.). The most common use in Flask is to specify the URL route with that.

Save the changes with *Ctrl+S*. Click into your terminal and type 

```bash
flask run 
```
The Flask built-in development web server should show up. Now hold down *Ctrl* and *left-click* on the URL *127.0.0.1:5000*. It should open your standard browser at that URL with a *Hello, World!* message. 






- [](https://www.example.com)






---
## Sources
---
- https://code.visualstudio.com/docs/python/python-tutorial
- https://www.youtube.com/watch?v=dam0GPOAvVI&t=4255s
- notebook "03d - How to set up Python and VS Code" from the class "316002 Entwicklung von Web-Anwendungen" of Prof. Dr. Alexander Eck. 
- the notebook "03b - Full stack web dev intro notebook" from the class "316002 Entwicklung von Web-Anwendungen" by Prof. Dr. Alexander Eck.
- https://pythonbasics.org/decorators/

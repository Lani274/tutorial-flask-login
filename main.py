from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #to run a flaks application, a running webserver
    # only if we run main.py not install it, we are going to execute this line debug=true
    # you want this because if you import main.py from another file and you dont have this lines, it will run the webserver
    # you only want to run the webserver if this file runs directly if_name==main
    # app.run will run my flask application and it will say debug=true
    # which means everytime we will make a change in our python code it will automatically run the webserver
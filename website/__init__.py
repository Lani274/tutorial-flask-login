from flask import Flask

def create_app():
    app = Flask (__name__)
    app.config['SECRET_KEY'] = 'dsjkajeijw'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app


# import and register the blueprints here, and that they contain some views for our application
# all of these url files that are stored in these url files access them
# no prefixes
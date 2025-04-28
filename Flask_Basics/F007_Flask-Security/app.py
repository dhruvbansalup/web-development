from flask import Flask
from flask_restful import Api
from application.database import db


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['DEBUG'] = True


db.init_app(app)
api=Api(app)
app.app_context().push()

from application import controllers
from application import api

if __name__ == '__main__':
    app.run(debug=True)
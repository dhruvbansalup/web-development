import os
from flask import Flask

from flask_restful import Resource, Api

from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

app = None
api=None
def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api=Api(app)
    app.app_context().push()
    return app,api

app,api = create_app()

# Import all the controllers so they are loaded
from application.controllers import *

#Add all restful Controllers
from application.api import userAPI,AllTableViewAPI
api.add_resource(userAPI,"/api/user","/api/user/<string:username>") 
api.add_resource(AllTableViewAPI,"/api/table/<string:table>")


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8080)

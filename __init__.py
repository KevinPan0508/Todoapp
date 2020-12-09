from flask import Flask
from .extensions import mongo
from .main.routes  import main
import urllib

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://kevin:'+ urllib.parse.quote_plus('kanrhel0508@') +'@localhost:38080/flaskapp?authSource=admin'
   # app.config['MONGO_URI'] = 'mongodb://localhost:38080/flaskapp'
   # app.config['MONGO_HOST'] = 'localhost'
   # app.config['MONGO_PORT'] = 38080
   # app.config['MONGO_USERNAME'] = 'kevin'
   # app.config['MONGO_PASSWORD'] = 'kanrhel0508@'
    mongo.init_app(app)
    app.register_blueprint(main)
    return app

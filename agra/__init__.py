
### Standard Library Imports ###
import os
################################

### 3rd Party Imports ###
from flask import Flask 
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.pymongo import PyMongo
from flask.ext.admin import Admin
#################################

### Local Imports ###

#################################


bootstrap = Bootstrap()
mail = Mail()
mongo = PyMongo()
admin = Admin()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = "/"

def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), "config", config_name + ".py")
    app.config.from_pyfile(cfg)
    bootstrap.init_app(app)
    mongo.init_app(app)
    admin.init_app(app)
    db.init_app(app)
    lm.init_app(app)
    from .apps.main import main
    from .apps.products import products
    app.register_blueprint(main)
    app.register_blueprint(products, url_prefix = '/products')
    return app
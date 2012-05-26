from flask import Flask
app = Flask(__name__)
#shortcut for adding new urls
url = app.add_url_rule

#Database construction
from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
#show the queries, which are build behind the scenes
db.engine.echo = True

#ini code
import scheduler.urls
import scheduler.models

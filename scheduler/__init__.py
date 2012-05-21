from flask import Flask
app = Flask(__name__)
#shortcut for adding new urls
url = app.add_url_rule



#boilerplate ini code
import scheduler.urls

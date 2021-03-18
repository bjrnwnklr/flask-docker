from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# do any additional configuration stuff, instantiation (e.g. of DBs, encryption, API objects) here
# and import them in the respective modules.

# this has to be at the bottom to avoid circular references
from flaskexampleapp import routes

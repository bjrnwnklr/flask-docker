from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# this has to be at the bottom to avoid circular references
from flaskexampleapp import routes

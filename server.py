from os import environ
from flask import Flask

app = Flask(__name__)
port = int(environ.get('PORT', 33507))
app.run(port=port)

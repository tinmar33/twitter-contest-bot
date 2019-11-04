from os import environ
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get('PORT', 33507))
app.run(port=port)

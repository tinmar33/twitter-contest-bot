from os import environ
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get('PORT'))
app.run(host='0.0.0.0', port=port)

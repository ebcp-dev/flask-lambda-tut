from flask import Flask
app = Flask(__name__)


@app.routes("/")
def hello():
    return "Hello World!"

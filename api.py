import os
os.environ["PYTHON_VERSION"] = "3.9.11"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {
        "message": "hello world"
    }
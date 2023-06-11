from flask import Flask
app = Flask(__name__)
app.config['PYTHON_VERSION'] = "3.9.11"


@app.route('/')
def hello_world():
    return {
        "message": "hello world"
    }
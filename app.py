from flask import Flask
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    url = request.args.get('url').url
    return url

if __name__ == '__main__':
    app.run()

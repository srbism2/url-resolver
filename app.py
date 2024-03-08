from flask import Flask
import requests
from flask_cors import CORS
from flask import request, jsonify
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    url = request.args.get('url')
    url1 = requests.get(url).url
    return url1

if __name__ == '__main__':
    app.run()

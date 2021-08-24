from flask import Flask
import socket
import os

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    return hostname


@app.route('/healthz')
def health():
    return "healthy"


@app.route('/ready')
def ready():
    return "ready"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("PORT"), debug=os.environ.get("DEBUG"))

import flask
from utils import get_secret

app = flask.Flask(__name__)

@app.route('/health')
def health():
  return "Healthy JSON!"

@app.route('/secret')
def secret():
  return get_secret()

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
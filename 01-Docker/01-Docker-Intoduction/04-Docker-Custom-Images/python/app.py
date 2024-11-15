from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
     return 'Hello, World!'


@app.route("/info")
def info():
     return 'Welcome to the world of Docker based Python WebServer'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
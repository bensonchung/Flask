from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "TEST!"

@app.route("/github")
def github():
    return "github!"

if __name__ == "__main__":
    app.run()

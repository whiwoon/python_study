from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/home")
def home():
    return render_template("home.html", name="whiwoon")


if __name__ == "__main__":
    app.run()

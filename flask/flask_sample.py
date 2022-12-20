from flask import Flask, render_template, request
from modules.timesTable import cal

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def search():
    num = int(request.args.get("num"))
    result = cal(num)
    return render_template("result.html", calNum=num, calResult=result)


if __name__ == "__main__":
    app.run(port=8000)

from flask import Flask, render_template, request, redirect
from modules.timesTable import cal

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def search():
    num = request.args.get("num")
    if num == "" or num == None:
        return redirect("/")
    result = cal(num)
    return render_template("result.html", calNum=num, calResult=result)


if __name__ == "__main__":
    app.run(port=8000)

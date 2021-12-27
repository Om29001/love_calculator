from flask import Flask, render_template, request, flash
from cal import Calmain
from DB import dataget, dataput, datadel

app = Flask(__name__)


@app.route("/<user>")
def hello_name(user):
    return render_template("hello.html", name=user)


@app.route("/nooneknows/admin", methods=["GET", "POST"])
def admin():
    navigation=dataget()
    try:
        print("1")
        if request.method == "POST":
            print("1")
            option = request.form['options']
            print(option)
            datadel(int(option))
        navigation=dataget()
        return render_template("admin.html", navigation = navigation)
    finally:
        return render_template("admin.html", navigation = navigation)


@app.route("/", methods=["GET", "POST"])
def new_student():
    k = 0
    if request.method == "POST":    
        a = request.form["name1"]
        m = request.form["name2"]
        k = Calmain(a, m)
        dataput(a, m,k)
    return render_template("love.html", result=k)


@app.route("/info")
def info():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)

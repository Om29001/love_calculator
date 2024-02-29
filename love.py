from flask import Flask, render_template, request, send_from_directory
from cal import Calmain

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def new_student():
    k = 0
    if request.method == "POST":    
        a = request.form["name1"]
        m = request.form["name2"]
        k = Calmain(a, m)
    return render_template("love.html", result=k)

# Serve ads.txt from the root route
@app.route("/ads.txt")
def ad():
    return send_from_directory(app.static_folder, "ads.txt")

@app.route("/info/ads.txt")
def ad2():
    return send_from_directory(app.static_folder, "ads.txt")

@app.route("/info")
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug=True)

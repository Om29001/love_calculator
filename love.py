from flask import Flask, render_template, redirect, url_for, request
from cal import Calmain
app = Flask(__name__)

@app.route('/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)


@app.route('/', methods =["GET", "POST"])
def new_student():
    k = 0
    if request.method == 'POST':
        a = request.form['name1']
        m = request.form['name2']
        k = Calmain(a,m)
    return render_template('love.html', result = k)

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
   app.run(debug = True)
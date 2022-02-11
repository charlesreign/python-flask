from os import abort
from flask import Flask, flash, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = "Drmhze6EPcv0fN_81Bj-nA"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Try again'
        else:
            flash('You lwere successfully logged in')
            flash('logout before login')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)
    

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = "f9bf78b9a18ce6d46a0cd2b0b86df9da"

@app.route("/")
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
            "<br> <a href= '/logout> click here to logout </a></br>"
    return "You are not logged in <br> <a href='/login'><br>"+ \
        "click here to login <br></a>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    # this removes the username rom the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
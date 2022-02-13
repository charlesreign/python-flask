from os import abort
from flask import Flask, flash, session, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///student.sqlite3'
app.config['SECRET_KEY']='f9bf78b9a18ce6d46a0cd2b0b86df9da'
db = SQLAlchemy(app)

class student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,  pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route("/")
def show_all():
    return render_template('show_all.html', students = student.query.all())

@app.route('/new', methods=['POST','GET'])
def new():
    if request.method == "POST":
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all fields', 'error')
        else:
            stu = student(
                request.form['name'],
                request.form['city'],
                request.form['addr'],
                request.form['pin'],
            )
            db.session.add(stu)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

    

if __name__ == "__main__":
    app.run(debug=True)
from os import abort
from flask import Flask, flash, session, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/upload")
def upload():
    return render_template('index.html')

@app.route('/uploader', methods=['POST','GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file upload successful'
    

if __name__ == "__main__":
    app.run(debug=True)
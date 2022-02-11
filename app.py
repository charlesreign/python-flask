from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'username@email.com'
app.config['MAIL_PASSWORD'] = 'password'

@app.route("/")
def index():
    msg = Message("Hello world", sender='charlesgold45@gmail.com', recipients=['username@email.com'])
    msg.body = "Hello world this is a message sent using flask mail"
    mail.send(msg)
    return "Message sent"


if __name__ == "__main__":
    app.run(debug=True)
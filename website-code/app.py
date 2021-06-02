from flask import Flask, render_template, request, session, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SWLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/generic')
def generic():
    return render_template('generic.html')


@app.route('/ian-roberts')
def ianroberts():
    return render_template('ian-roberts.html')


@app.route('/toby-sykes')
def tobyskyes():
    return render_template('toby-sykes.html')


@app.route('/websites')
def websites():
    return render_template('websites.html')


@app.route('/hosting')
def hosting():
    return render_template('hosting.html')


@app.route('/consulting')
def consulting():
    return render_template('consulting.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        session.permanent - True
        user = request.form["username"]
        session["username"] = user

        found_user = users.query.filter_by(username=user).first()
        if found_user:
            session["username"] = found_user.username
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.comit()

        flash("Login Succesful!")
        return redirect(url_for("/"))
    else:
        if "user" in session:
            flash("Already Logged in")
            return redirect(url_for("login"))
        return render_template('register.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')


@app.route("/db")
def database():
    return render_template("db.html", values=users.query.all())


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)

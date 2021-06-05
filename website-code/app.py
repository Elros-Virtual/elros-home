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


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["user"]
        session["user"] = user
        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
        return render_template('login.html')


# @app.route('/register', methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         user = request.form["user"]
#         session["user"] = user
#         return redirect(url_for(login))
#     else:
#         return render_template('register.html')


@app.route('/user', methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route('/myaccount')
def myaccount():
    if "user" in session:
        user = session["user"]
        return render_template('myaccount.html')
    else:
        return redirect(url_for("login"))


@app.route('/logout')
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/db")
def database():
    return render_template("db.html", values=users.query.all())


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)

from flask import Flask, render_template, request, session, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
# app.permanent_session_lifetime = datetime(days=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SWLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self):
        return '<name %r>' % self.id


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
    # if request.method == "POST":
    #     session.permanent = True
    #     user = request.form["user"]
    #     session["user"] = user

    #     found_user = users.query.filter_by(name=user).first()
    #     if found_user:
    #         session["email"] = found_user.email
    #     else:
    #         usr = users(user, "")
    #         db.session.add(usr)
    #         db.session.commit()

    #     flash("Login Succesful!")
    #     return redirect(url_for("myaccount"))
    # else:
    #     if "user" in session:
    #         flash("Already logged in")
    #         return redirect(url_for("myaccount"))
    return render_template('login.html')


# @app.route('/register', methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         user = request.form["user"]
#         email = request.form["email"]
#         session["user"] = user
#         session["email"] = email

#         found_user = users.query.filter_by(name=user).first()
#         found_user.email = email
#         if found_user:
#             session["email"] = found_user.email
#             session["user"] = found_user.user
#         else:
#             usr = users(user, "")
#             db.session.add(usr)
#             db.session.commit()

#         return redirect(url_for(login))
#     else:
#         return render_template('register.html')

@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":
        name = request.form.get("name")
        new_user = users(name=name)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/register')
        except:
            return "There was an error"

    else:
        user_list = users.query.order_by(users.date_created)
        return render_template('register.html', user_list=user_list)


@app.route('/myaccount', methods=["POST", "GET"])
def myaccount():
    email = None
    if "user" in session:
        user = session["user"]
        # email = session["email"]
        return render_template('myaccount.html', user=user)
    else:
        return redirect(url_for("login"))


@app.route('/logout')
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/db")
def database():
    return render_template("db.html", values=users.query.all())


if __name__ == '__main__':
    db.create_all()
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)

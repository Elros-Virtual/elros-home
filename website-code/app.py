from flask import Flask, render_template, request
from flask_sendgrid import SendGrid

app = Flask(__name__)
app.config['SENDGRID_API_KEY'] = 'apikey'
app.config['SENDGRID_DEFAULT_FROM'] = 'hello@elrosvirtual.co.uk'
mail = SendGrid(app)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        mail.send_email(to_email=email,
                        subject='Thank you for your Contact', text=message)

        return render_template('index.html')

    # else:
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


@app.route('/cicd')
def cicd():
    return render_template('cicd.html')


@app.route('/consulting')
def consulting():
    return render_template('consulting.html')


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/websites')
def websites():
    return render_template('generic.html')


@app.route('/hosting')
def hosting():
    return render_template('generic.html')


@app.route('/cicd')
def cicd():
    return render_template('generic.html')


@app.route('/digitalsolutions')
def digitalsolutions():
    return render_template('generic.html')


@app.route('/Consulting')
def Consulting():
    return render_template('generic.html')


@app.route('/mobileapps')
def mobileapps():
    return render_template('generic.html')


@app.route('/toby-sykes')
def tobyskyes():
    return render_template('toby-sykes.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)

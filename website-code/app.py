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
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)

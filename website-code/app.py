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


@app.route('/toby-skyes')
def tobyskyes():
    return render_template('toby-skyes.html')


if __name__ == '__main__':
    app.run(debug=True)

# , host='0.0.0.0'

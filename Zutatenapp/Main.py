from flask import Flask
from flask import render_template

app = Flask("Zutatenapp")


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/franz')
def franz():
    return render_template('franz.html')


@app.route('/italy')
def italy():
    return render_template('italy.html')


@app.route('/turkey')
def turkey():
    return render_template('turkey.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask
from flask import render_template
from libs import data

app = Flask("Zutatenapp")
rezepte = {}
rezepte = data.create_dummy_data()

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add_franz')
def add_franz():
    return render_template('add_franz.html')


@app.route('/add_italy')
def add_italy():
    return render_template('add_italy.html')


@app.route('/add_turkey')
def add_turkey():
    return render_template('add_turkey.html')

@app.route('/summary_franz')
def summary_franz():
    return render_template('summary_franz.html', rezepte=rezepte['franz'])


@app.route('/summary_italy')
def summary_italy():
    return render_template('summary_italy.html', rezepte=rezepte['italy'])


@app.route('/summary_turkey')
def summary_turkey():
    return render_template('summary_turkey.html', rezepte=rezepte['turkey'])

@app.route('/add_richtung')
def add_richtung():
    return render_template('add_richtung.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
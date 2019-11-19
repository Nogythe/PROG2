from flask import Flask
from flask import render_template
from libs import data
from flask import request
from flask import redirect
from flask import url_for

app = Flask("Zutatenapp")
rezepte = {}
rezepte = data.create_dummy_data()

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add_franz')
def add_franz():
    return render_template('add_franz.html')


@app.route('/add_italy', methods=['GET', 'POST'])
def add_italy():
    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezept_beschreibung = request.form['rezept_beschreibung']
        rezepte[rezept_titel] = rezept_beschreibung
        return redirect(url_for('summary_italy'))

    return render_template('add_italy.html')


@app.route('/add_turkey')
def add_turkey():
    return render_template('add_turkey.html', methods=['GET', 'POST'])

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
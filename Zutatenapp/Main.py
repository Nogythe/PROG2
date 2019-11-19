import os
from pathlib import Path
from flask import Flask
from flask import render_template
from libs import data
from flask import request
from flask import redirect
from flask import url_for

app = Flask("Zutatenapp")
app_main_path = Path(os.path.abspath("/".join(os.path.realpath(__file__).split("/")[:-1])))
data_path = Path(os.path.abspath(app_main_path / "data"))
data_storage_file = data_path / "rezepte.json"

rezepte = {}
#rezepte = data.create_dummy_data()
rezepte = data.load_json(data_storage_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_gericht")
def add_gericht():
    return render_template("add_gericht.html")

@app.route('/add_franz', methods=['GET', 'POST'])
def add_franz():
    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezept_beschreibung = request.form['rezept_beschreibung']
        if not 'franz' in rezepte:
            rezepte['franz'] = {}
        rezepte['franz'][rezept_titel] = rezept_beschreibung
        data.save_json(data_storage_file, rezepte)
        return redirect(url_for('summary_franz'))

    return render_template('add_franz.html')


@app.route('/add_italy', methods=['GET', 'POST'])
def add_italy():
    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezept_beschreibung = request.form['rezept_beschreibung']
        if not 'italy' in rezepte:
            rezepte['italy'] = {}
        rezepte['italy'][rezept_titel] = rezept_beschreibung
        data.save_json(data_storage_file, rezepte)
        return redirect(url_for('summary_italy'))

    return render_template('add_italy.html')


@app.route('/add_turkey', methods=['GET', 'POST'])
def add_turkey():
    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezept_beschreibung = request.form['rezept_beschreibung']
        if not 'turkey' in rezepte:
            rezepte['turkey'] = {}
        rezepte['turkey'][rezept_titel] = rezept_beschreibung
        data.save_json(data_storage_file, rezepte)
        return redirect(url_for('summary_turkey'))

    return render_template('add_turkey.html', methods=['GET', 'POST'])







@app.route('/summary_franz')
def summary_franz():

    return render_template('summary_franz.html', rezepte=rezepte['franz'])


@app.route('/summary_italy')
def summary_italy():
    if 'italy' in rezepte:
        return render_template('summary_italy.html', rezepte=rezepte['italy'])
    else: 
        return render_template('summary_italy.html', rezepte=None)


@app.route('/summary_turkey')
def summary_turkey():
    return render_template('summary_turkey.html', rezepte=rezepte['turkey'])



if __name__ == '__main__':
    app.run(debug=True, port=5000)
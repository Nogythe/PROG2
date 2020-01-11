import os
from pathlib import Path
from flask import Flask
from flask import render_template
from libs import data
from flask import request
from flask import redirect
from flask import url_for

"""
Attribute:
app: Name der Applikation
app_main_path: Pfad wo die App liegt im Betriebssystem
data_path: Ordner in welchem das JSON File in der App-Struktur liegt
data_storage_file: zusammengesetzter, kompletter Pfad inkl Filename des JSON-Files in dem die Daten gespeichert sind
"""

app = Flask("Zutatenapp")
app_main_path = Path(os.path.abspath(
    "/".join(os.path.realpath(__file__).split("/")[:-1])))
data_path = Path(os.path.abspath(app_main_path / "data"))
data_storage_file = data_path / "rezepte.json"

rezepte = {}
# rezepte = data.create_dummy_data()


@app.route("/")
def home():
    """
    Route und Funktion für die Startseite
    Daten werden geladen und Statistiken, welche auf der Startseite angezeigt werden, werden berechnet und mitgeschickt

    Returns:
        render_template: Das template index.html wird mit allen nötigen Daten gerendert
    """
    rezepte = data.load_json(data_storage_file)

    # calculating some statistic facts
    count_italy = int(len(rezepte['italy']))
    count_franz = int(len(rezepte['franz']))
    count_turkey = int(len(rezepte['turkey']))
    count_total = count_italy + count_franz + count_turkey

    percent_italy = round(count_italy / count_total * 100, 1)
    percent_franz = round(count_franz / count_total * 100, 1)
    percent_turkey = round(count_turkey / count_total * 100, 1)

    return render_template("index.html", count_total=count_total, count_italy=count_italy, count_franz=count_franz, count_turkey=count_turkey, percent_italy=percent_italy, percent_franz=percent_franz, percent_turkey=percent_turkey)


@app.route("/add_gericht")
def add_gericht():
    """
    Route und Funktion für die Unterseite zur Auswahl welche Art von Rezept hinzugefügt werden möchte

    Returns:
        render_template: Das template add_gericht.html wird gerendert
    """
    return render_template("add_gericht.html")


@app.route('/add_franz', methods=['GET', 'POST'])
def add_franz():
    """
    Route und Funktion für das Erstellen eines neuen französischen Rezeptes
    Entweder wird das Formualr zur Eingabe angezeigt (GET) oder der Eintrag wird gespeichert (POST)

    Returns:
        render_template: Das template add_franz.html wird gerendert (Anzeige Formular zur Eingabe)
        redirect: Wenn ein Eintrag gespeichert wurde (POST), wird auf die Anzeige aller französischen Rezepte weitergeleitet
    """
    rezepte = data.load_json(data_storage_file)

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
    """
    Route und Funktion für das Erstellen eines neuen italienischen Rezeptes
    Entweder wird das Formualr zur Eingabe angezeigt (GET) oder der Eintrag wird gespeichert (POST)

    Returns:
        render_template: Das template add_italy.html wird gerendert (Anzeige Formular zur Eingabe)
        redirect: Wenn ein Eintrag gespeichert wurde (POST), wird auf die Anzeige aller italienischen Rezepte weitergeleitet
    """
    rezepte = data.load_json(data_storage_file)

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
    """
    Route und Funktion für das Erstellen eines neuen türkischen Rezeptes
    Entweder wird das Formualr zur Eingabe angezeigt (GET) oder der Eintrag wird gespeichert (POST)

    Returns:
        render_template: Das template add_turkey.html wird gerendert (Anzeige Formular zur Eingabe)
        redirect: Wenn ein Eintrag gespeichert wurde (POST), wird auf die Anzeige aller türkischen Rezepte weitergeleitet
    """
    rezepte = data.load_json(data_storage_file)

    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezept_beschreibung = request.form['rezept_beschreibung']
        if not 'turkey' in rezepte:
            rezepte['turkey'] = {}
        rezepte['turkey'][rezept_titel] = rezept_beschreibung
        data.save_json(data_storage_file, rezepte)
        return redirect(url_for('summary_turkey'))

    return render_template('add_turkey.html', methods=['GET', 'POST'])


@app.route('/summary_franz', methods=['GET', 'POST'])
def summary_franz():
    """
    Route und Funktion für die Anzeige aller französischen Gerichte
    Entweder werden alle Rezepte angezeigt (GET) oder ein Rezept wird gelöscht (POST)

    Returns:
        render_template: Das template summary_franz.html wird gerendert (Anzeige aller französischen Rezepte)
    """
    rezepte = data.load_json(data_storage_file)

    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezepte['franz'].pop(rezept_titel, None)
        data.save_json(data_storage_file, rezepte)

    return render_template('summary_franz.html', rezepte=rezepte['franz'])


@app.route('/summary_italy', methods=['GET', 'POST'])
def summary_italy():
    """
    Route und Funktion für die Anzeige aller italienischen Gerichte
    Entweder werden alle Rezepte angezeigt (GET) oder ein Rezept wird gelöscht (POST)

    Returns:
        render_template: Das template summary_italy.html wird gerendert (Anzeige aller italienischen Rezepte)
    """
    rezepte = data.load_json(data_storage_file)

    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezepte['italy'].pop(rezept_titel, None)
        data.save_json(data_storage_file, rezepte)

    if 'italy' in rezepte:
        return render_template('summary_italy.html', rezepte=rezepte['italy'])
    else:
        return render_template('summary_italy.html', rezepte=None)


@app.route('/summary_turkey', methods=['GET', 'POST'])
def summary_turkey():
    """
    Route und Funktion für die Anzeige aller türkischen Gerichte
    Entweder werden alle Rezepte angezeigt (GET) oder ein Rezept wird gelöscht (POST)

    Returns:
        render_template: Das template summary_turkey.html wird gerendert (Anzeige aller türkischen Rezepte)
    """
    rezepte = data.load_json(data_storage_file)

    if request.method == 'POST':
        rezept_titel = request.form['rezept_titel']
        rezepte['turkey'].pop(rezept_titel, None)
        data.save_json(data_storage_file, rezepte)

    return render_template('summary_turkey.html', rezepte=rezepte['turkey'])


if __name__ == '__main__':
    app.run(debug=True, port=5000)

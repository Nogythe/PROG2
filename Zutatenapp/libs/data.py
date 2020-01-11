"""
Summary:
data.py ist eine Library welche sämtliche Interaktionen mit dem JSON-File abwickelt
"""
import json


def load_json(json_path):
    """
    Laedt alle Rezepte aus dem JSON File

    Args:
        json_path (string): Pfad wo das JSON File liegt
    Returns:
        dict: Dict mit allen Rezepten
    """
    try:
        with open(json_path) as open_file:
            rezepte = json.load(open_file)
    except FileNotFoundError:
        rezepte = {}

    return rezepte


def save_json(json_path, data):
    """
    Speichert alle Rezepte in dem JSON File

    Args:
        json_path (string): Pfad wo das JSON File liegt
        data (dict): Alle Rezepte, die im JSON File abgespeichert werden soll
    """
    with open(json_path, "w+", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)



def create_dummy_data():
    """
    Erstellen von dummy Daten, welche zur Entwicklung benötigt wurden

    Returns:
        dict: Dict mit Dummmy-Daten
    """
    rezepte = {
        'italy': {
			'Spaghetti': 'Beschreibung adasdiubasida',
			'Penne': 'Text'
        },
		'franz': {
			'Frosch': 'Beschreibung adasdiubasida',
			'Baguette': 'Text'
        },
		'turkey': {
			'Frosch': 'Beschreibung adasdiubasida',
			'Baguette': 'Text'
        }
    }
    return rezepte
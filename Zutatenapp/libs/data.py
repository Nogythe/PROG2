import json


def load_json(json_path):
    try:
        with open(json_path) as open_file:
            rezepte = json.load(open_file)
    except FileNotFoundError:
        rezepte = {}

    return rezepte


def save_json(json_path, data):
    with open(json_path, "w+", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)



def create_dummy_data():
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
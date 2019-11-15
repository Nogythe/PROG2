from flask import Flask
from flask import render_template

app = Flask("Zutatenapp")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/Franz')
def Franz():
	return render_template('franz.html')

@app.route('/Italy')
def Italy():
	return render_template('franz.html')

@app.route('/Turkey')
def Turkey():
	return render_template('franz.html')

if __name__ == "_main_":
	app.run(debug=True, port=5000)

	"""Neu"""

	menu = [
        ('Neues Rezept', add),
        ('Zeige Rezepte', show)
    ]

    from collections import defaultdict as DefaultDict
import json

def load():
    try:
        with open('recipes.txt') as file_:
            recipes = DefaultDict(list, json.load(file_))
    except IOError:
        recipes = DefaultDict(list)
    return recipes

def save(recipes):
    with open('recipes.txt', 'w') as file_:
        json.dump(recipes, file_)

def get_category(prompt, recipes):
    categories = recipes.keys()
    for number, name in enumerate(categories):
        print '{:2d}: {}'.format(number, name)
    category = raw_input(prompt)
    try:
        category = categories[int(category)]
    except (ValueError, IndexError):
        pass
    return category

def add(recipes):
    try:
        recipe = raw_input('Ihr Rezepttext (Ctrl-C beendet): ')
    except KeyboardInterrupt:
        return
    category = get_category(
        'Unter welche Kategorie faellt Rezept? ', recipes
    )
    recipes[category].append(recipe)

def show(recipes):
    if recipes:
        category = get_category(
            'Aus welcher Kategorie sollen Rezepte gezeigt werden? ', recipes
        )
        for recipe in recipes[category]:
            print '\n{}\n***\n'.format(recipe)
    else:
        print 'Keine Rezepte vorhanden!\n'

def run():
    menu = [
        ('Neues Rezept', add),
        ('Zeige Rezepte', show)
    ]
    recipes = load()
    while True:
        print
        for item_number, item in enumerate(menu):
            print '{:2d}: {}'.format(item_number, item[0])
        try:
            choice = int(raw_input('Ihre Wahl (Ctrl-C beendet): '))
        except (ValueError, IndexError):
            print 'Bitte gueltige Nummer eingeben...',
        except KeyboardInterrupt:
            break
        print
        menu[choice][1](recipes)
    save(recipes)
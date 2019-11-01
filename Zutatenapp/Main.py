from flask import Flask
from flask import render_template

app = Flask("Zutatenapp")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/franz')
def franz():
	return render_template('franz.html')

if __name__ == "_main_":
	app.run(debug=True, port=5000)
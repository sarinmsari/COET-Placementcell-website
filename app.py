from flask import render_template,Flask

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html')

#leaving rest of the functions for hacktoberfest participants

if __name__ == '__main__':
	app.run(debug=True)
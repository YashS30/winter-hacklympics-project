from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/languages')
def languages_page():
	return render_template('languages.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	if request.method == 'POST':
		# When the form is submitted, redirect to the home page
		return redirect(url_for('home_page'))
	else:
		# Otherwise, show the login form
		return render_template('login.html')

if __name__ == "__main__":
	app.run(debug=True)
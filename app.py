from flask import Flask, render_template, request, url_for, redirect
from language_descriptions import languages

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
	return render_template('home.html')

@app.route('/about', methods=['GET'])
def about_page():
	return render_template('about.html')

@app.route('/languages', methods=['GET'])
def languages_page():
	return render_template('language_list.html', languages=languages)

@app.route('/languages/<lang>', methods=['GET'])
def language_page(lang):
	# Checks if the url language is in our list of languages
	if lang in languages:
		return render_template('language.html', language=lang, description=languages[lang]['description'])
	else:
		return redirect(url_for('home_page'))

@app.route('/recommender', methods=['GET', 'POST'])
def recommender_page():
	if request.method == 'GET':
		return render_template('recommender.html')
	else:
		answers = []
		for i in range(1, 7):
			try:
				answers.append(request.form['question' + str(i)] == 'yes')
			except:
				answers.append(False)
		
		if answers[0]:
			language = 'Javascript'
			reason = 'You should learn HTML, CSS, and Javascript. They are the 3 languages needed to create a good website!'
		elif answers[1]:
			language = 'Python'
			reason = 'Python is arguably the best language for data science and machine learning. It is also a very beginner friendly language, making it great to get started with!'
		elif answers[2]:
			language = 'C#'
			reason = 'C# is used for programming in the Unity game engine, which is a good game engine to begin with.'
		elif answers[3]:
			language = 'C'
			reason = 'C is an incredibly fast low-level language. This makes it great for things that lack processing power, like Arduino and other microchips. You may also want to consider C++.'
		elif answers[4]:
			language = 'C#'
			reason = 'C# is what Microsoft recommends for Windows desktop applications. This makes sense because C# was created by Microsoft. Learning C# will familiarize you with object oriented programming as well!'
		elif answers[5]:
			language = 'Javascript'
			reason = 'Javascript is becoming increasingly popular at the backend because of a runtime called Node.js which is great for server side programming!'
		else:
			language = 'Python'
			reason = 'Python is the best language to learn for beginners due to its easy-to-read sytax and ease of setup!'

		return render_template('form_submitted.html', language=language, reason=reason, description=languages[language]['description'])


if __name__ == "__main__":
	app.run(debug=True)

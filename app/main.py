from flask import Flask, render_template, request, redirect
from flask_wtf import Form
from wtforms import TextField
from thumb_links import get_thumb_links
import requests

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def front():
	return render_template('front.html')


@app.route('/results', methods = ['GET', 'POST'])
def results():
	username = request.args.get('username', '')
	return render_template('results.html', username=username)

@app.route('/reverse', methods = ['GET', 'POST'])
def reverse():
	img_link = request.form.get('img_link', '')
        return render_template('reverse.html', img_link=img_link)

if __name__ == "__main__":
        app.run(debug=True)

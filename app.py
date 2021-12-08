from flask import Flask, render_template, request
import numpy as np
import api # To load functions in api.py
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

HOST = os.getenv('HOST')
PASSWORD = os.getenv('PASSWORD')
API_KEY = os.getenv('API_KEY')

DATABASE = 'movie'
USERNAME = 'admin'
PORT = 3306

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        api_data = api.load_data()
        return render_template('index.html', data = api_data)

if __name__ == "__main__":
    app.run(debug=True)
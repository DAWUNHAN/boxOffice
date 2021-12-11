from dotenv import load_dotenv
from flask import Flask, render_template, request
import numpy as np
import api # To load functions in api.py
import ml
import os
import sys
import pickle
from dotenv import load_dotenv
import json
import csv
import pandas as pd 

with open('model.pkl','rb') as pickle_file:
    model = pickle.load(open('model.pkl', 'rb'))

load_dotenv(verbose=True)

API_KEY = os.getenv('API_KEY')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    df = api.csv_to_df('./data/movie_train.csv')
    if request.method == 'GET':
        return render_template('index.html', df=df, API_KEY=API_KEY)


    if request.method == 'POST':
        result = request.form
        Year = float(request.form['Year'])
        imdbRating = float(request.form['imdbRating'])
        pred_office =  ml.predict_boxoffice(Year=Year,  imdbRating=imdbRating)
        
        print(result['Year'])

        return render_template('index.html',  pred_office=pred_office, df=df, API_KEY=API_KEY)

if __name__ == "__main__":
    app.run(debug=True)

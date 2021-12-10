from dotenv import load_dotenv
from flask import Flask, render_template, request
import numpy as np
import api # To load functions in api.py
import ml
import os
import sys
import pickle
from lightgbm import LGBMRegressor
# load_dotenv(verbose=True)

# HOST = os.getenv('HOST')
# PASSWORD = os.getenv('PASSWORD')
# API_KEY = os.getenv('API_KEY')

# DATABASE = 'movie'
# USERNAME = 'admin'
# PORT = 3306

# app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(error):
# 	return render_template('404.html'), 404

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         api_data = api.load_data()
#         return render_template('index.html', data = api_data)


# if __name__ == "__main__":
#     app.run(debug=True)



# load_dotenv(verbose=True)

# HOST = os.getenv('HOST')
# PASSWORD = os.getenv('PASSWORD')
# API_KEY = os.getenv('API_KEY')

# DATABASE = 'movie'
# USERNAME = 'admin'
# PORT = 3306
 


app = Flask(__name__)
# with open('model.pkl','rb') as pickle_file:
#     model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        result = request.form
        # print(result['Name'])
        pred =  ml.predict_boxoffice(Year=2020, Director='Wes Anderson', Language='English', Country='USA', imdbRating=8.5, Genre_single='Romance')
        print(pred)
        return render_template('index.html', result=result)


 
if __name__ == "__main__":
    app.run(debug=True)

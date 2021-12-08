# import requests
# from flask import Flask

# app = Flask(__name__)
# API_KEY = '1549868c'

# title = 'Avatar'
# movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&t='+title).json()


# @app.route('/')
# def index():
#     return movieInfo['BoxOffice']
import os
import requests
import pandas as pd
import sys
import pymysql
from dotenv import load_dotenv
import json

load_dotenv(verbose=True)

HOST = os.getenv('HOST')
PASSWORD = os.getenv('PASSWORD')
API_KEY = os.getenv('API_KEY')

DATABASE = 'movie'
USERNAME = 'admin'
PORT = 3306


def connect_db(host, port, database, username, password):
    try:
        conn = pymysql.connect(host=host,user=username, password=password,db=database, port=port, use_unicode=True, charset='utf8') 
        cursor = conn.cursor()
        print('connected to DB')
    except:
        print('not connected to DB')
        sys.exit(1)
        
    return conn, cursor


def load_csv(path):
    csv_id = pd.read_csv(path)
    return csv_id

def load_api(movie_id):
    for i in range (len(csv_id)):
        movie_id = csv_id.iloc[i]['tconst']
        try:
            movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&i='+movie_id).json()
            print(movieInfo['Title'])
        except:
            pass
    return movieInfo

def api_to_db():
    conn, cursor = connect_db(HOST, PORT, DATABASE, USERNAME, PASSWORD)

    # cursor.execute("DROP TABLE IF EXISTS movie_train;")
    # cursor.execute("""CREATE TABLE movie_train (
    #                     imdbID VARCHAR(100) PRIMARY KEY,
    #                     Title VARCHAR(100) NOT NULL,
    #                     Year INT,
    #                     Genre VARCHAR(100),
    #                     Director VARCHAR(100),
    #                     Language VARCHAR(100),
    #                     Country VARCHAR(100),
    #                     Poster VARCHAR(100),
    #                     imdbRating FLOAT(3, 2),
    #                     BoxOffice VARCHAR(100) NOT NULL
    #     );
    #     """)

    for i in range (len(csv_id)):
        movie_id = csv_id.iloc[i]['tconst']
        try:
            movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&i='+movie_id).json()
            if(movieInfo['BoxOffice'] != 'N/A'):
                cursor.execute("""INSERT INTO movie_train (imdbID, Title, Year, Genre, Director, Language, Country, Poster,  imdbRating, BoxOffice) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                    (movieInfo['imdbID'], movieInfo['Title'], movieInfo['Year'], 
                    movieInfo['Genre'], movieInfo['Director'], movieInfo['Language'], movieInfo['Country'], movieInfo['Poster'], 
                    movieInfo['imdbRating'], movieInfo['BoxOffice']))
        except:
            pass

    conn.commit()


# csv_id = load_csv('./data/imdb_20941.csv')
# api_to_db()

# load_api(csv_id)
# connect_db(HOST, PORT, DATABASE, USERNAME, PASSWORD)

def load_data():
    conn, cursor = connect_db(HOST, PORT, DATABASE, USERNAME, PASSWORD)

    cursor.execute("""SELECT *
                    FROM movie_train
                    WHERE imdbID = 'tt0449851'
    """)
    fields = map(lambda x:x[0], cursor.description)
    result = [dict(zip(fields,row))   for row in cursor.fetchall()]
    # data = json.dumps(cursor.fetchall())
    # return data

    print(result)
    conn.close()
    return result

load_data()
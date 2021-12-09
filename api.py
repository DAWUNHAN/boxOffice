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
import csv

load_dotenv(verbose=True)

HOST = os.getenv('HOST')
PASSWORD = os.getenv('PASSWORD')
API_KEY = os.getenv('API_KEY')

DATABASE = 'movie'
USERNAME = 'admin'
PORT = 3306

# AWS mySQL DB 연결하기
def connect_db(host, port, database, username, password):
    try:
        conn = pymysql.connect(host=host,user=username, password=password,db=database, port=port, use_unicode=True, charset='utf8') 
        cursor = conn.cursor()
        print('connected to DB')
    except:
        print('not connected to DB')
        sys.exit(1)
        
    return conn, cursor

# csv file 불러오기
def load_csv(path):
    csv_id = pd.read_csv(path)
    return csv_id

def load_api(movie_id, csv_id):
    for i in range (len(csv_id)):
        movie_id = csv_id.iloc[i]['tconst']
        try:
            movieInfo = requests.get('http://www.omdbapi.com/?apikey='+API_KEY+'&i='+movie_id).json()
            print(movieInfo['Title'])
        except:
            pass
    return movieInfo

# API에 있는 데이터를 DB에 입력하는 함수.
def api_to_db(conn, cursor, csv_id):
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
            print(movieInfo['imdbID'])
        except:
            pass

    conn.commit()

# AWS DB로부터 데이터를 받아오는 함수.
def load_data():
    conn, cursor = connect_db(HOST, PORT, DATABASE, USERNAME, PASSWORD)
    cursor.execute("""SELECT *
                    FROM movie_train
                    WHERE imdbID = 'tt0449851'
    """)
    fields = map(lambda x:x[0], cursor.description)
    result = [dict(zip(fields,row)) for row in cursor.fetchall()]
    conn.close()
    return result

# DB 특정 테이블 데이터를 csv 파일로 가져오기 
def db_to_csv(conn, cursor, TABLE):
    column = []
    cursor.execute("SHOW FULL COLUMNS FROM %s " %TABLE)
    rows = cursor.fetchall()
    for i in range(len(rows)):
        column.append(rows[i][0])

    cursor.execute("SELECT * FROM %s" %TABLE)
    rows = cursor.fetchall()
    rows = list(rows)
    for i in range(len(rows)):
        rows[i] = list(rows[i])

    f = open('./data/%s.csv' %TABLE, 'w', encoding='utf-8', newline="")
    wr = csv.writer(f)
    wr.writerow(column)

    for i in range(len(rows)):
        wr.writerow(rows[i])
    f.close()
    conn.close()



conn, cursor = connect_db(HOST, PORT, DATABASE, USERNAME, PASSWORD)
# csv_id = load_csv('./data/imdb_20310.csv')
# api_to_db(conn, cursor, csv_id)
# db_to_csv(conn, cursor, 'movie_train')


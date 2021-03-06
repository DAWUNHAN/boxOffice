import pandas as pd
import numpy as np
import pickle


def predict_boxoffice(Year, imdbRating):
    with open('model.pkl','rb') as pickle_file:
        model = pickle.load(open('model.pkl', 'rb'))

    df = pd.DataFrame(
        data=[[Year, imdbRating]], 
        columns=['Year', 'imdbRating']
    )
    # 예측
    pred = round(model.predict(df)[0], 2)
    pred = format(pred, ',')

    return pred


    
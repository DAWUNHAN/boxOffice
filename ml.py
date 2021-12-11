import pandas as pd
import numpy as np
import pickle
from category_encoders import OneHotEncoder


def predict_boxoffice(Year, imdbRating ):
    with open('model.pkl','rb') as pickle_file:
        model = pickle.load(open('model.pkl', 'rb'))

    df = pd.DataFrame(
        data=[[Year, imdbRating]], 
        columns=['Year', 'imdbRating']
    )
    ohEncoder = OneHotEncoder()
    df_encoded = ohEncoder.fit_transform(df)

    # 예측
    pred = model.predict(df_encoded)[0]
    
    return pred


    
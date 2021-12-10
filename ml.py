import pandas as pd
import numpy as np
import pickle
from category_encoders import OneHotEncoder

# def predict_boxoffice(model, Year, Director, Language, Country, imdbRating, Genre_single ):
#     df = pd.DataFrame(
#         data=[[Year, Director, Language, Country, imdbRating, Genre_single]], 
#         columns=['Year', 'Director', 'Language', 'Country', 'imdbRating', 'Genre_single']
#     )
#     ohEncoder = OneHotEncoder()
#     df_encoded = ohEncoder.fit_transform(df)
#     # 예측
#     pred = np.expm1(model.predict(df_encoded)[0])
#     return pred

# def predict_boxoffice(model, Year, Director, Language, Country, imdbRating, Genre_single ):
    
#     df = pd.DataFrame(
#         data=[[Year, Director, Language, Country, imdbRating, Genre_single]], 
#         columns=['Year', 'Director', 'Language', 'Country', 'imdbRating', 'Genre_single']
#     )

#     # 예측
#     pred = np.expm1(model.predict(df)[0])
    
#     return pred

def predict_boxoffice(Year, Director, Language, Country, imdbRating, Genre_single ):
    with open('model.pkl','rb') as pickle_file:
        model = pickle.load(open('model.pkl', 'rb'))
    df = pd.DataFrame(
        data=[[Year, Director, Language, Country, imdbRating, Genre_single]], 
        columns=['Year', 'Director', 'Language', 'Country', 'imdbRating', 'Genre_single']
    )
    ohEncoder = OneHotEncoder()
    df_encoded = ohEncoder.fit_transform(df)

    # 예측
    pred = np.expm1(model.predict(df_encoded, predict_disable_shape_check=True)[0])
    
    return pred
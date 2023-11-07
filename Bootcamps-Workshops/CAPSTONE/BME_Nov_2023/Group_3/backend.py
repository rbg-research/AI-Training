# To install:
# pip install uvicorn
# pip install fastapi
# pip install pandas

# To run: uvicorn service:app --host 0.0.0.0 --port 8007

import pickle

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd 
import numpy as np
# Added import for pandas

app = FastAPI()

# Load the trained model from the pickle file
with open('chr.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)

def predict_kideny_disease(features):
#     try:
    prediction = clf.predict([features])[0]
    return prediction
#     except Exception as e:
#         return str(e)

@app.post("/predict/")
async def predict_kidney_disease(data: dict):
    # Convert the input data to a pandas DataFrame
    bp = data['bp']
    sg= data['sg']
    Al= data['Al']  
    Su=data['Su']
    Rbc=data['Rbc']
    Bu=data['Bu']
    Sc=data['Sc']
    Sod=data['Sod']
    Pot=data['Pot']
    Hemo=data['Hemo']
    Wbcc=data['Wbcc']
    Rbcc=data['Rbcc']
    Htn=data['Htn']





    # Feature selection and preprocessing (you may need to adjust this part)
    # Assuming the columns in your DataFrame match the expected feature names
    #features = input_data[['Bp', 'Sg', 'Al', 'Su', 'Rbc', 'Bu', 'Sc', 'Sod', 'Pot', 'Hemo', 'Wbcc', 'Rbcc', 'Htn']]
    features_array = np.array([bp,sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn])
    # Make predictions using the loaded model
    prediction = predict_kideny_disease(features_array)
    print(prediction)

    # Assuming 'Class' column is used for predictions
    return JSONResponse(content={"features": prediction}, status_code=200)


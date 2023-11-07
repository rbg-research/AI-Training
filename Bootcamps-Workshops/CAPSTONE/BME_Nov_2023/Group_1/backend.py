# To install :
# pip install uvicorn
# pip install fastapi
# pip install python-multipart
# pip install Pillow

# To run: uvicorn service:app --host 0.0.0.0 --port 8000

import pickle
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# Load the trained model from the pickle file
with open('breastcancerprediction.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)

def preprocess_data(data):
    # Assuming 'data' is a dictionary containing feature values
    df = pd.DataFrame(data, index=[0])
    X = df.values  # Convert to a NumPy array
    # Standardize the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    return X

@app.post("/predict/")
async def predict_cancer(data: dict):
    try:
        X = preprocess_data(data)
        prediction = clf.predict(X)[0]
        return JSONResponse(content={"prediction": int(prediction)}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

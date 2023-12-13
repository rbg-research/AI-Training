#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To install :
# pip install uvicorn
# pip install fastapi
# pip install python-multipart
# pip install Pillow

# To run: uvicorn BackEnd:app --host 0.0.0.0 --port 8000
import pandas as pd
import pickle
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
from io import BytesIO
import cv2
from scipy import stats 
from sklearn.preprocessing import StandardScaler
app = FastAPI()

# Load the trained model from the pickle file
with open('Final-KNN.pkl', 'rb') as model_file:
    clf = pickle.load(model_file)

def process_image(image):
    # Open the uploaded image using Pillow (PIL)
    img = Image.open(image)
    img = img.convert("L")
    
#     # Resize and convert to grayscale (if not already)
#     img = img.resize((28, 28)).convert('L')
    
#     # Convert to a NumPy array
#     img_array = np.array(img).flatten()  # Flatten to match the model input shape
    
#     # Standardize the data
#     img_array = (img_array - np.mean(img_array)) / np.std(img_array)
    
#     return img_array


#     img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # Load as grayscale

    # Extract features from the image (mean, median, mode, standard deviation, skewness, and kurtosis)
    mode_result = stats.mode(img, axis=None, keepdims=True)
    featureVector = [
        np.mean(img),
        np.median(img),
        float(mode_result[0]),  # Mode calculation
        np.std(img),
        np.nan_to_num(np.float64(stats.skew(np.array(img).flatten()))),
        np.nan_to_num(np.float64(stats.kurtosis(np.array(img).flatten())))
    ]

    # Define the header for the CSV file
    header = ['Mean', 'Median', 'Mode', 'StandardDeviation', 'Skewness', 'Kurtosis']  # Update with your actual feature names

    # Create a Pandas DataFrame with the features
    b = pd.DataFrame([featureVector], columns=header)
    ss = StandardScaler()
    a = ss.fit_transform(b)

    y_pred = clf.predict(a)
    print(y_pred)
    if(y_pred == [1]):
        return 'Pituitary'
    if(y_pred == [2]):
        return 'No Tumor'
    if(y_pred == [3]):
        return 'Meningioma'
    if(y_pred == [4]):
        return 'Glioma'
    
@app.post("/predict/")
async def predict_disorder(file: UploadFile):
    try:
        prediction = process_image(BytesIO(await file.read()))
#         prediction = clf.predict([img_array])[0]
        return JSONResponse(content={"class": prediction}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


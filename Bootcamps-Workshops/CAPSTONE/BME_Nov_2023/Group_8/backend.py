# To install :
# pip install uvicorn
# pip install fastapi
# pip install python-multipart
# pip install Pillow

# To run: uvicorn service:app --host 0.0.0.0 --port 8000

import numpy as np
import pickle
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Load the trained stress level prediction model from the pickle file
with open('stress-level-prediction.pkl', 'rb') as model_file:
    stress_level_model = pickle.load(model_file)
    
def predict_bmi(features):
    try:
        prediction = stress_level_model.predict(np.array(features).reshape(1,-1))[0]
        return prediction
    except Exception as e:
        return str(e)

@app.post("/predict/")
async def predict_stress_level(features:dict):
    # Prepare the data as a dictionary or a list
#         input_data = [[humidity, temperature]]
    print("/n/n/n/n/n/n",features["Humidity"],features["Temperature"],"/n/n/n/n/n/n")

    features_array = [features["Humidity"],features["Temperature"]]
    

#         input_data = np.array([data["humidity"], data["temperature"]).reshape(1,-1)

    # Make a prediction using the loaded model
#         prediction = stress_level_model.predict([input_data])
    prediction = predict_bmi(features_array)
    print("prediction: ", prediction)
    if prediction == 0:
        return JSONResponse(content={"predicted_stress": "Low"}, status_code=200)
    elif prediction == 1:
        return JSONResponse(content={"predicted_stress": "Medium"}, status_code=200)
    else:
        return JSONResponse(content={"predicted_stress": "High"}, status_code=200)
#     except Exception as e:
#         print(e)
#         return e
#         raise HTTPException(status_code=500, detail=str(e))
# #         raise "hello"
                               
                               
                               
                               
                               
# # To install :
# # pip install uvicorn
# # pip install fastapi
# # pip install python-multipart
# # pip install Pillow

# # To run: uvicorn service:app --host 0.0.0.0 --port 8000

# import pickle
# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import JSONResponse
# import numpy as np
# from io import BytesIO

# app = FastAPI()

# # Load the trained model from the pickle file
# with open('stress-level-prediction.pkl', 'rb') as model_file:
#     clf = pickle.load(model_file)

# def predict_bmi(features):
#     try:
#         prediction = clf.predict([features])[0]
#         return prediction
#     except Exception as e:
#         return str(e)

# @app.post("/predict/")
# async def predict_bmi_from_features(features: dict):
#     try:
#         height = features['height']
#         weight = features['weight']
#         age = features['age']
#         gender = features['gender']

#         # Preprocess the features (you can add more preprocessing if needed)
#         features_array = np.array([height, weight, age, gender])

#         prediction = predict_bmi(features_array)
#         return JSONResponse(content={"BMI": prediction}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)


    

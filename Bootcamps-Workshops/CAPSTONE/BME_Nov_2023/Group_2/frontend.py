import streamlit as st
import requests
import numpy as np
import json

st.title("Heart Disease Prediction")

st.write("Enter the following information for prediction:")

# Create input fields for features
age = st.number_input("Your age", min_value=20, max_value=100, value=20)
sex = st.number_input("Your sex", min_value=0, max_value=1, value=1)
cp = st.number_input("Do you experience chest pain?", min_value=0, max_value=4, value=1)
trestbps = st.number_input("Your resting blood pressure", min_value=80, max_value=350, value=81)
chol = st.number_input("Your serum cholesterol", min_value=120, max_value=600, value=120)
fbs = st.number_input("Is your fasting blood sugar above 120mg/dL", min_value=0, max_value=1, value=1)
restecg = st.number_input("Your resting ECG results", min_value=0, max_value=3, value=1)
thalach = st.number_input("What is your maximum heart rate", min_value=60, max_value=300, value=60)
exang = st.number_input("Ever experienced exercise-induced angina?", min_value=0, max_value=1, value=1)
oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value=0, max_value=8, value=1)
slope = st.number_input("Enter the slope of the peak exercise ST segment", min_value=0, max_value=3, value=1)
ca = st.number_input("The number of major vessels (0-3) colored by fluoroscopy", min_value=0, max_value=4, value=1)
thal = st.number_input("Enter accordingly: 0 = normal; 1 = fixed defect; 2 = reversible defect", min_value=0, max_value=3, value=1)

# Create a dictionary with user input data
data = {
    'age': age,
    'sex': sex,
    'cp': cp,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs,
    'restecg': restecg,
    'thalach': thalach,
    'exang': exang,
    'oldpeak': oldpeak,
    'slope': slope,
    'ca': ca,
    'thal': thal,
}
# ... (previous code)

# Use the custom encoder when serializing
# Convert the NumPy array to a Python list
data_list = data.tolist()

json_data = json.dumps(data_list)

# Now, use `json_data` in the request.
if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict/", json=json_data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        result = "Positive for Heart Disease" if prediction == 1 else "Negative for Heart Disease"
        st.write(f"Prediction: {result}")
    else:
        st.error("Failed to make a prediction. Please try again.")

if st.button("Predict"):
    # Make a POST request with the JSON data
    url = "http://localhost:8000/predict/"  # Adjust the URL to your prediction endpoint
    headers = {'Content-Type': 'application/json'}

    # Use json.dumps to convert the data dictionary to a JSON string
    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers=headers)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        result = "Positive" if prediction == 1 else "Negative"
        st.write(f"Prediction: {result}")
    else:
        st.error("Failed to make a prediction. Please try again.")

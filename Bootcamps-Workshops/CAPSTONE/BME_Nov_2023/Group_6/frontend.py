# To install; pip install streamlit
# To run:  streamlit run frontend.py

import streamlit as st
import requests

st.title("Diabetes Prediction")

st.write("Enter the following information for prediction:")

# Create input fields for features
i_d = st.number_input("patients id ")
age = st.number_input("Age")
gender = st.number_input("Gender")
height = st.number_input("Height(cm)")
weight = st.number_input("Weight(kg)")
ap_hi = st.number_input("Diastolic Blood Pressure(mmHg) ")
ap_lo= st.number_input("Systolic Blood Pressure(mmHg)")
cholestrol = st.number_input("Cholestrol(dL)")
glc = st.number_input("Glucose(mg/dL)")
smk = st.number_input("Smoke")
alc = st.number_input("Alcohol")
active = st.number_input("Active")
cardio = st.number_input("Cardio")

# Create a dictionary with user input data
data = {
    'id': i_d,
    'age': age,
    'gender': gender,
    'height': height,
    'weight': weight,
    'ap_hi': ap_hi,
    'ap_lo': ap_lo,
    'cholestrol': cholestrol,
    'glc': glc,
    'smk': smk,
    'alc': alc,
    'active': active,
    'cardio': cardio,
    
}

if st.button("Predict"):
    response = requests.post("http://localhost:8001/predict/", json=data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        result = "Person has cardio vascular disease" if prediction == 1 else "Person has no cardio vascular disease"
        st.write(f"Prediction: {result}")
    else:
        st.error("Failed to make a prediction. Please try again.")

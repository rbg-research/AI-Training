# To install; pip install streamlit
# To run:  streamlit run frontend.py

import streamlit as st
import requests

st.title("hepatitis c prediction")

st.write("Enter the following information for prediction:")

# Create input fields for features
age = st.number_input("age") 
sex = st.number_input("sex")
ALB = st.number_input("ALB")
ALP = st.number_input("ALP")
ALT = st.number_input("ALT")
AST = st.number_input("AST")
BIL = st.number_input("BIL")
CHE = st.number_input("CHE")
CHOL= st.number_input("CHOL")
CREA= st.number_input("CREA")
GGT = st.number_input("GGT")
PROT= st.number_input("PROT")
# Create a dictionary with user input data
data = {
    'age': age,
    'sex': sex,
    'ALB': ALB,
    'ALP': ALP,
    'ALT': ALT,
    'AST': AST,
    'BIL': BIL,
    'CHE': CHE,
    'CHOL': CHOL,
    'CREA': CREA,
    'GGT': GGT,
    'PROT': PROT,
}

if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict/", json=data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        result = "HEALTHY BLOOD DONOR" if prediction == 1 else "SUSPECTED BLOOD DONOR"
        st.write(f"Prediction: {result}")
    else:
        st.error("Failed to make a prediction. Please try again.")

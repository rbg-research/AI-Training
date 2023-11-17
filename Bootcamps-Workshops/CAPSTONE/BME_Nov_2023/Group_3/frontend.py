# To install; pip install streamlit
# To run:  streamlit run frontend.py

import streamlit as st
import pandas as pd
import requests  # Add this import for the 'requests' library

st.title("Kidney Disease Classifier")


# Create input fields for tabular data
st.sidebar.header("Enter Tabular Data")
st.sidebar.markdown("Please enter the values for the following features:")
bp = st.sidebar.number_input("bp")
sg = st.sidebar.number_input("sg")
Al = st.sidebar.number_input("Al")
Su = st.sidebar.number_input("Su")
Rbc = st.sidebar.number_input("Rbc")
Bu = st.sidebar.number_input("Bu")
Sc = st.sidebar.number_input("Sc")
Sod = st.sidebar.number_input("Sod")
Pot = st.sidebar.number_input("Pot")
Hemo = st.sidebar.number_input("Hemo")
Wbcc = st.sidebar.number_input("Wbcc")
Rbcc = st.sidebar.number_input("Rbcc")
Htn = st.sidebar.number_input("Htn")

# Create a dictionary from the input data
input_data = {
    "bp": bp,
    "sg": sg,
    "Al": Al,
    "Su": Su,
    "Rbc": Rbc,
    "Bu": Bu,
    "Sc": Sc,
    "Sod": Sod,
    "Pot": Pot,
    "Hemo": Hemo,
    "Wbcc": Wbcc,
    "Rbcc": Rbcc,
    "Htn": Htn
}

if st.button("Classify"):
    response = requests.post("http://localhost:8516/predict/", json=input_data)
    if response.status_code == 200:
        data = response.json()
        st.write(f"Predicted Class: {data['class']}")
    else:
        st.error("Failed to classify the data. Please try again.")



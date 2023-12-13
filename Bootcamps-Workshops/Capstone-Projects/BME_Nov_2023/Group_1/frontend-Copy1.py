# To install; pip install streamlit
# To run:  streamlit run frontend.py

import streamlit as st
import requests

st.title("Breast cancer risk Prediction")

st.write("Enter the following information for prediction:")

# Create input fields for features
radius_mean = st.number_input("Radius Mean")
texture_mean = st.number_input("Texture Mean")
perimeter_mean = st.number_input("Perimeter Mean")
area_mean = st.number_input("Area Mean")
smoothness_mean = st.number_input("Smoothness Mean")
compactness_mean = st.number_input("Compactness Mean")
concavity_mean = st.number_input("Concavity Mean")
concave_points_mean = st.number_input("Concave Points Mean")
symmetry_mean = st.number_input("Symmetry Mean")
fractal_dimension_mean = st.number_input("Fractal Dimension Mean")
radius_se = st.number_input("Radius SE")
texture_se = st.number_input("Texture SE")
perimeter_se = st.number_input("Perimeter SE")
area_se = st.number_input("Area SE")
smoothness_se = st.number_input("Smoothness SE")
compactness_se = st.number_input("Compactness SE")
concavity_se = st.number_input("Concavity SE")
concave_points_se = st.number_input("Concave Points SE")
symmetry_se = st.number_input("Symmetry SE")
fractal_dimension_se = st.number_input("Fractal Dimension SE")
radius_worst = st.number_input("Radius Worst")
texture_worst = st.number_input("Texture Worst")
perimeter_worst = st.number_input("Perimeter Worst")
area_worst = st.number_input("Area Worst")
smoothness_worst = st.number_input("Smoothness Worst")
compactness_worst = st.number_input("Compactness Worst")
concavity_worst = st.number_input("Concavity Worst")
concave_points_worst = st.number_input("Concave Points Worst")
symmetry_worst = st.number_input("Symmetry Worst")
fractal_dimension_worst = st.number_input("Fractal Dimension Worst")

# Create a dictionary with user input data
data = {
    'radius_mean': radius_mean,
    'texture_mean': texture_mean,
    'perimeter_mean': perimeter_mean,
    'area_mean': area_mean,
    'smoothness_mean': smoothness_mean,
    'compactness_mean': compactness_mean,
    'concavity_mean': concavity_mean,
    'concave_points_mean': concave_points_mean,
    'symmetry_mean': symmetry_mean,
    'fractal_dimension_mean': fractal_dimension_mean,
    'radius_se': radius_se,
    'texture_se': texture_se,
    'perimeter_se': perimeter_se,
    'area_se': area_se,
    'smoothness_se': smoothness_se,
    'compactness_se': compactness_se,
    'concavity_se': concavity_se,
    'concave_points_se': concave_points_se,
    'symmetry_se': symmetry_se,
    'fractal_dimension_se': fractal_dimension_se,
    'radius_worst': radius_worst,
    'texture_worst': texture_worst,
    'perimeter_worst': perimeter_worst,
    'area_worst': area_worst,
    'smoothness_worst': smoothness_worst,
    'compactness_worst': compactness_worst,
    'concavity_worst': concavity_worst,
    'concave_points_worst': concave_points_worst,
    'symmetry_worst': symmetry_worst,
    'fractal_dimension_worst': fractal_dimension_worst
}

if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict/", json=data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        result = "malignant" if prediction == 1 else "benign"
        st.write(f"Prediction: {result}")
    else:
        st.error("Failed to make a prediction. Please try again.")

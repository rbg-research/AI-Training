import streamlit as st
import requests

# Define the FastAPI API endpoint URL
api_url = "http://localhost:8000/predict/"  # Update with your actual FastAPI server URL

# Define your custom feature names
feature_names = [
    'mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension'
]

label_names = {0: "malignant", 1: "benign"}  # Update with your actual label names

# Create a Streamlit web app
st.title("Cancer Cell Detection")

st.write("Enter the feature values for prediction:")

# Create input fields for each feature using your custom feature names
feature_values = {}
for feature_name in feature_names:
    feature_values[feature_name] = st.number_input(feature_name)

if st.button("Predict"):
    # Make a POST request to the FastAPI API
    data = {feature_name: value for feature_name, value in feature_values.items()}
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.write(f"Prediction: {prediction}")
    else:
        st.error("Error occurred during prediction. Please check the input data.")

# You can add more Streamlit elements, like charts or explanations, as needed.

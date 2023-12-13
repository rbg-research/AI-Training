# To install; pip install streamlit
# To run:  streamlit run frontend.py

import streamlit as st
import requests

st.title("Stress Prediction App")

# Collect input data
st.write("Please enter the following information:")
humidity = st.number_input("Humidity", value=0.0)
temperature = st.number_input("Temperature", value=0.0)
step_count = st.number_input("Step Count", value=0)
# stress_level = st.number_input("Stress Level", value=0)

features = {
        "Humidity": humidity,
        "Temperature": temperature,
        "Step Count": step_count,
#         "Stress Level": stress_level
    }

if st.button("Predict Stress Level"):
    # Prepare the data as a dictionary
    

    # Make a request to your prediction API
    response = requests.post("http://localhost:8000/predict/", json=features)

    if response.status_code == 200:
        prediction = response.json()
#         st.write(prediction)
        st.write(f"Predicted Stress Level: {prediction['predicted_stress']}")
    else:
        st.error("Failed to predict stress level. Please try again.")
        
        

        




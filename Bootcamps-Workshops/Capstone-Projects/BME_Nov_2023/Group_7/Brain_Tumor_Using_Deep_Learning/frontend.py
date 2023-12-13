#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To install; pip install streamlit
# To run:  streamlit run frontend.py

import streamlit as st
import requests

st.title("Brain Tumor Detecion And Classification")

uploaded_file = st.file_uploader("Upload a digit image...", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    if st.button("Classify"):
        response = requests.post("http://localhost:8000/predict/", files={"file": uploaded_file})
        if response.status_code == 200:
            data = response.json()
            st.write(f"Predicted Label: {data['label']}")
        else:
            st.error("Failed to classify the image. Please try again.")


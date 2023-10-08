import streamlit as st
import requests
import os  # Import the os module for file handling

st.title("BMI App")

uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("classify"):
        # Check if the 'uploads' directory exists, and create it if not
        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        # Save the uploaded file to the 'uploads' directory
        with open(os.path.join("uploads", uploaded_file.name), 'wb') as file:
            file.write(uploaded_file.read())

        # Set the path to the saved image
        image_path = os.path.join("uploads", uploaded_file.name)

        # Now send the image to the server for transcription
        files = {'file': (uploaded_file.name, open(image_path, 'rb'), 'image/png')}
        
        #"http://13.233.246.91:7008/BMI"

        response = requests.post('http://13.233.246.91:7008/BMI', files=files)

        if response.status_code == 200:
            response_data = response.json()
            st.json(response_data)
        elif response.status_code == 422:
            st.error(f"Validation error: {response.content}")
        else:
            st.error(f"Error: Unable to transcribe data. Status code: {response.status_code}")

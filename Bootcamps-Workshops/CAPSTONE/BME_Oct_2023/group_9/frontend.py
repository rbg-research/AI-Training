# streamlit.py
import streamlit as st
import requests
import os  # Import the os module for file handling

st.title("OCR Transcription App")

uploaded_file = st.file_uploader("Upload an image file")

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Transcribe"):
        # Check if the 'uploads' directory exists, and create it if not
        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        # Save the uploaded file to the 'uploads' directory
        with open(os.path.join("uploads", uploaded_file.name), 'wb') as file:
            files = {'image': (uploaded_file.name, uploaded_file.read(), 'image/jpeg')}
            
            response = requests.post('http://13.233.246.91:7009/upload', files=files)
            if response.status_code == 200:
                st.json({"status done":"done"})
            elif response.status_code == 422:
                st.error(f"Validation error: {response.content}")
            else:
                st.error(f"Error: Unable to transcribe data. Status code: {response.status_code}")
txt=st.text_input("enter_id")
print(txt)
if st.button("Extract"):
    response = requests.get(f'http://13.233.246.91:7009/extract_data/?unique_id={txt}')
    if response.status_code == 200:
        st.json(response.text)
    elif response.status_code == 422:
        st.error(f"Validation error: {response.content}")
    else:
        st.error(f"Error: Unable to transcribe data. Status code: {response.status_code}")

            
            


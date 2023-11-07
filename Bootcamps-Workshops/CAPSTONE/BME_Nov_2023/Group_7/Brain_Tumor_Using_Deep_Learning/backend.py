import io
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
#uvicorn BackEnd:app --host 0.0.0.0 --port 8000
app = FastAPI()

# Load the Keras model
loaded_model = load_model("braintumor1500.h5")

# Define class labels (modify as needed)
class_labels = {0: 'glioma', 1: 'meningioma', 2: 'no_tumor', 3: 'pituitary'}

def process_image(image_data):
    # Load the image using Keras preprocessing
    img = image.load_img(io.BytesIO(image_data), target_size=(240, 240))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    img = np.reshape(img, (1, 240, 240, 3))  # Reshape the image
    return img

@app.post("/predict/")
async def predict_image(file: UploadFile):
    # Read and process the uploaded image
    image_data = await file.read()

    # Ensure the image is reshaped to the expected shape
    img = process_image(image_data)

    # Make predictions using the loaded Keras model
    predictions = loaded_model.predict(img)

    # Get the predicted class
    predicted_class = int(np.argmax(predictions))  # Convert to a regular Python integer

    # Get the class label of the predicted class
    predicted_label = class_labels.get(predicted_class, "Unknown")

    return JSONResponse(content={"class": predicted_class, "label": predicted_label}, status_code=200)

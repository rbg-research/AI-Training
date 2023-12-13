import io
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = FastAPI()

# Load the Keras model
loaded_model = load_model("vgg19_model_trained.h5")

# Define class labels (modify as needed)
class_labels = {0: 'parasite', 1: 'uninfected'}

def process_image(image_data):
    # Load the image using Keras preprocessing
    img = image.load_img(io.BytesIO(image_data), target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

@app.post("/predict/")
async def predict_image(file: UploadFile):
    # Read and process the uploaded image
    image_data = await file.read()
    img = process_image(image_data)

    # Make predictions using the loaded Keras model
    predictions = loaded_model.predict(img)

    # Get the predicted class
    predicted_class = int(np.argmax(predictions))  # Convert to regular Python integer

    # Get the class label of the predicted class
    predicted_label = class_labels.get(predicted_class, "Unknown")

    return JSONResponse(content={"class": predicted_class, "label": predicted_label}, status_code=200)

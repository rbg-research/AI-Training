# To install :
# pip install uvicorn
# pip install fastapi
# pip install python-multipart
# pip install Pillow

# To run: uvicorn service:app --host 0.0.0.0 --port 8000

import pickle
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
from tensorflow.keras.models import Model, load_model,Sequential
from io import BytesIO
from tensorflow.keras.preprocessing import image
app = FastAPI()

# Load the trained model from the pickle file
# with open('FOOT_ULCER.pkl', 'rb') as model_file:
#     clf = pickle.load(model_file)
    
clf=load_model('./weight.h5')

def process_image(image):
    # Open the uploaded image using Pillow (PIL)
    img = Image.open(image)
    
    # Resize and convert to grayscale (if not already)
    img = img.resize((224, 224)).convert('L')
    
    # Convert to a NumPy array
    img_array = np.array(img).flatten()  # Flatten to match the model input shape
    
    # Standardize the data
    img_array = (img_array - np.mean(img_array)) / np.std(img_array)
    
    return img_array
def prediction(path):
    t=['infection','ischemia']
#     img = Image.open(image)
    img=image.load_img(path, target_size=(224,224))
    img=image.img_to_array(img)
    img=img/255
    img=np.expand_dims(img,axis=0)
    p=clf.predict(img)

    if(p<0.5):
        p=0
    else:
        p=1
    return f"The image is of a {t[p]}"
    

@app.post("/predict/")
async def predict(file: UploadFile):
#     try:
    t=['infection','ischemia']
    #         img=image.load_img(BytesIO(await file.read()), target_size=(224,224))
#     img=image.img_to_array(BytesIO(await file.read()))
      
#     img = process_image(BytesIO(await file.read()))
    res=prediction(BytesIO(await file.read()))
    
#     img = Image.open(BytesIO(await file.read()))
#     img=image.load_img(img, target_size=(224,224))
#     img=image.img_to_array(img)
#     img=img/255
#     img=np.expand_dims(img,axis=0)
#     p=clf.predict(img)
#     if(p<0.5):
#         p=0
#     else:
#         p=1

#     #       prediction = clf.predict([img_array])[0]
    return JSONResponse(content={"class": res}, status_code=200)
#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=500)
    
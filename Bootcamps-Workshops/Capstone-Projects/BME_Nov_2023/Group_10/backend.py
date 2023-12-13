from fastapi import FastAPI, HTTPException
import pickle
import numpy as np

app = FastAPI()

# Load the trained model from the pickle file
with open("cancercelldetection.pkl", "rb") as file:
    model = pickle.load(file)

@app.post("/predict/")
async def predict(data: dict):
    try:
        # Extract features from the request data
        feature_vector = []
        for feature_name in feature_names:
            feature_vector.append(data.get(feature_name, 0.0))
        
        # Make a prediction using the trained model
        prediction = model.predict([feature_vector])
        
        # Convert the prediction to a human-readable label
        prediction_label = label_names[prediction[0]]

        return {"prediction": prediction_label}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)

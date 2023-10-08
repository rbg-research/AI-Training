# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import requests
import json
from io import BytesIO

app = FastAPI()

OCR_API_URL = 'http://13.233.246.91:8002/api/v1/transcribe'

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    headers = {
        'accept': 'application/json',
    }
    files = {
        'file': (file.filename, BytesIO(file.file.read()), 'image/jpeg'),
        'timestamps': (None, 's'),
        'is_digital': (None, ''),
    }

    response = requests.post(OCR_API_URL, headers=headers, files=files)

    if response.status_code == 200:
        response_data = response.json()
        with open('OCR.json', 'w') as json_file:
            json.dump(response_data, json_file)
        return JSONResponse(content=response_data)
    else:
        return JSONResponse(content={"error": f"Unable to read data. Status code: {response.status_code}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7002)

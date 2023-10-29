from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import requests
import json
from io import BytesIO
from summarize_text import generate_summary  # Assuming you have a function to generate a summary

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
        extracted_text = response_data.get('extracted_text', '')

        # Generate a summary from the extracted text
        summary = generate_summary(extracted_text)  # You need to implement or import a function to generate a summary

        # Save the summary to a file
        with open('summary.txt', 'w') as summary_file:
            summary_file.write(summary)

        # Return the summary as JSON response
        return JSONResponse(content={"summary": summary})
    else:
        return JSONResponse(content={"error": f"Unable to read data. Status code: {response.status_code}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7005)

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
import aiofiles
import shortuuid
import uvicorn
import pytesseract
import requests
from io import BytesIO


group_8 = FastAPI()

origins = ["*"]

group_8.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def Gettextfromimage(filename):
    OCR_API_URL = 'http://13.233.246.91:8006/api/v1/transcribe'
    headers = {
        'accept': 'application/json',
    }
    with open(filename, 'rb') as image_file:
        files = {
            'file': (image_file.name, image_file, 'image/jpeg'),
            'timestamps': (None, 's'),
            'is_digital': (None, ''),
        }

        response = requests.post(OCR_API_URL, headers=headers, files=files)
        if response.status_code == 200:
            print(response.text)
            return response.text
        else:
            print(response.status_code)
            return "Error"
async def save_file_locally(filename: str, file: "UploadFile") -> bool:
    """
    Save a file locally from an UploadFile object.

    Args:
        filename (str): The filename to save the file as.
        file (UploadFile): The UploadFile object.

    Returns:
        bool: Whether the file was saved successfully.
    """
    async with aiofiles.open(filename, "wb") as f:
        audio_bytes = await file.read()
        await f.write(audio_bytes)

    return True




def Callapi(text):
    print(text)
    api_url = 'http://13.233.246.91:8005/api/v1/classify'
    params = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'text': text,
        'labels': 'Under-weight,Normal,Over-weight,Obese',
        'timestamps': 's'
    }

    response = requests.post(api_url, params=params, data=data)
    if response.status_code == 200:
        print(response.text)
        return(response.text)
        # response_data = response.json()
        # with open('TC.json', 'w') as json_file:
        #     json.dump(response_data, json_file)
    else:
        print(f'Error:: {response.status_code}')
        return "error"
    
    
    


@group_8.post("/BMI")
async def process(file: UploadFile = File(...)):#text:str
    OCR_API_URL = 'http://13.233.246.91:8002/api/v1/transcribe'
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
        a=Callapi(response.text)
        return str(a)
    else:
        return f"Unable to read data. Status code: {response.status_code}"














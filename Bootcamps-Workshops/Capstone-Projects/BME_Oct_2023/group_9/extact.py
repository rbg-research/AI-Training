from fastapi import FastAPI, UploadFile, Form
from img2table.ocr import TesseractOCR
from img2table.document import Image
import cv2
from PIL import Image as PILImage
import pandas as pd
from fastapi.responses import FileResponse
import tempfile
import os

app = FastAPI()

# Initialize TesseractOCR
tesseract_ocr = TesseractOCR(n_threads=1, lang='eng')

@app.post("/upload/")
async def upload_image(image: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        temp_image.write(image.file.read())
        image_path = temp_image.name

    img = Image(src=image_path)

    # Extract tables
    extracted_tables = img.extract_tables(ocr=tesseract_ocr,
                                          implicit_rows=True,
                                          borderless_tables=True,
                                          min_confidence=50)

    # Process and return the extracted tables or save them to a file
    # For demonstration, we will save the extracted table to an Excel file
    table_file_path = "/tmp/tables.xlsx"
    img.to_xlsx(table_file_path, ocr=tesseract_ocr, implicit_rows=True, borderless_tables=True, min_confidence=50)

    return {"Status":"Done"}

@app.get("/extract_data/")
async def extract_data(unique_id: str):
    # Load the Excel file into a DataFrame
    df = pd.read_excel("/tmp/tables.xlsx")

    # Extract rows where the 'uniqueID' column matches the desired ID
    result = df[df['uniqueID'] == unique_id]

    return result.to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7009)

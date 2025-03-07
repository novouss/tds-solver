from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, status 
from fastapi.responses import JSONResponse
from fastapi import Form, File
from openai import OpenAI

import os

import submissions as sub

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DATA_PATH = "./data/"

URL = "https://llmfoundry.straive.com/openai/v1/"
KEY = os.environ["AIPROXY_TOKEN"]

client = OpenAI(
    base_url = URL,
    api_key = KEY
)

@app.post("/api/", status_code=status.HTTP_200_OK)
async def run(question: str = Form(...), file: UploadFile = File(...)):
    """
    Answer any graded assignment question and returns the result/answer for said question.
    
    Args:
        quesiton (str): The question of the user.
        file (file): The file the user is requesting to be downloaded/used.
        
    Returns:
        dict: Returns the answer based on user question.
    """
    filepath = DATA_PATH + file.filename
    
    with open(filepath, "wb") as f:
        f.write(await file.read())
    
    if file.filename.endswith(".zip"):
        files = sub.zipfile_extract(filepath, DATA_PATH)

    # respones = client.chat.completions.create(
    #     model = "gpt-4o-mini",
    #     messages = [{
    #         "role": "system",
    #         "content": "Reply only with the answer the user is looking for no added texts"
    #     },
    #     {
    #         "role": "user",
    #         "content": question
    #     }]
    # )
    
    # answer = respones.choices[0].message.content
    
    answer = {
        "question": question,
        "file_name": file.filename,
        "file_location": filepath,
        "files": files
    }
    
    return JSONResponse(content={ "answer": answer })

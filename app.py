from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, status 
from fastapi.responses import JSONResponse
from fastapi import Form, File

import chromadb
from authentication import client
from submissions import tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DATA_PATH = "./data/"

FUNCTIONS_DB = chromadb.PersistentClient(path="chromadb")
FUNC_COLLECTION = FUNCTIONS_DB.get_or_create_collection(name="functions")

@app.post("/api/", status_code=status.HTTP_200_OK)
async def run(question: str = Form(...), file: UploadFile = File(...)):
    """ Answer any graded assignment question and returns the result/answer for said question.
    
    Args:
        question (str): The question of the user.
        file (file): The file the user is requesting to be downloaded/used.
        
    Returns:
        dict: Returns the answer based on user question.
    """
    filepath = DATA_PATH + file.filename
    
    with open(filepath, "wb") as f:
        f.write(await file.read())
    
    if file.filename.endswith(".zip"):
        files = tasks["zipfile_extract"](filepath, DATA_PATH)

    # response = client.chat.completions.create(
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

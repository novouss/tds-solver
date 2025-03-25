from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, status 
from fastapi.responses import JSONResponse
from fastapi import Form, File

import os
import chromadb
from typing import Optional

import helpers.authentication as auth

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DATA_PATH = "./data"

FUNCTIONS_DB = chromadb.PersistentClient(path="chromadb")
FUNC_COLLECTION = FUNCTIONS_DB.get_or_create_collection(name="functions")

@app.post("/api/", status_code=status.HTTP_200_OK)
async def run(question: str = Form(...), file: Optional[UploadFile] = File(None)):
    """ Answer any graded assignment question and returns the result/answer for said question.
    
    Args:`
        question (str): The question of the user.
        file (file): The file the user is requesting to be downloaded/used.
        
    Returns:
        dict: Returns the answer based on user question.
    """

    # Creates the filepath for both extraction and retrieval
    if file:
        filepath = os.path.join(DATA_PATH, file.filename)
        # Creates the directory
        with open(filepath, "wb") as f:
            f.write(await file.read())

    answering = FUNC_COLLECTION.query(
        query_embeddings = auth.generate_embeddings(question),
        n_results = 1
    )

    docstring = answering["metadatas"][0][0]["docstring"]
    name = answering["documents"][0][0]
    function_call = auth.create_function_call(name, docstring)

    # response = auth.ask_tools(question, function_call)
    # answer = respones.choices[0].message.content
    
    answer = {
        "question": question,
        "name": name,
        "function_call": function_call,
        # "response": response
        # "answer": answering,
        # "file_name": file.filename,
        # "file_location": filepath,
    }
    
    return JSONResponse(content={ "answer": answer })

from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, UploadFile, status 
from fastapi import Form, File

import os
import json
import chromadb
from typing import Optional

import helpers.authentication as auth
import submissions as subs

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

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse("index.html")

@app.post("/api/", status_code=status.HTTP_200_OK)
async def run(question: str = Form(...), file: Optional[UploadFile] = File(None)):
    """ Answer any graded assignment question and returns the result/answer for said question.
    
    Args:
        question (str): The question of the user.
        file (file, optional): The file the user is requesting to be downloaded/used.
        
    Returns:
        dict: Returns the answer based on user question.
    """

    if file:
        filepath = os.path.join(DATA_PATH, file.filename)
        
        with open(filepath, "wb") as f:
            f.write(await file.read())
        
        question = f"The path is: {filepath}\n\n{question}"

    answering = FUNC_COLLECTION.query(
        query_embeddings = auth.generate_embeddings(question),
        n_results = 1
    )

    docstring = answering["metadatas"][0][0]["docstring"]
    name = answering["documents"][0][0]
    function_call = auth.create_function_call(name, docstring)

    response = auth.ask_tools(question, function_call)
    arguments = json.loads(response.function_call.arguments)
    # answer = subs.tasks[name](arguments)

    result = {
        "question": question,
        "function_called": name,
        # "function_call": function_call,
        "arguments": arguments,
        "response": json.loads(response),
        # "answer": answer,
        # "file_name": file.filename,
        # "file_location": filepath,
    }
    
    return JSONResponse(content={ "answer": result })

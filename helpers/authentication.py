
import os
from openai import OpenAI
from typing import List, Dict, Any

URL = "https://llmfoundry.straive.com/openai/v1/"
KEY = os.environ["AIPROXY_TOKEN"]

client = OpenAI(
    base_url = URL,
    api_key = KEY
)

model = "gpt-4o-mini"

def ask_something(prompt: str) -> str:
    response = client.chat.completions.create(
        model = model,
        messages = [
            { "role": "user", "content": prompt }
        ]
    )
    return response.choices[0].message.content

def ask_someone(system: str, prompt: str) -> str:
    response = client.chat.completions.create(
        model = model,
        messages = [
            { "role": "system", "content": system },
            { "role": "user", "content": prompt }
        ]
    )
    return response.choices[0].message.content

def generate_embeddings(text: str) -> List[float]:
    response = client.embeddings.create(
        input = text,
        model = "text-embedding-3-small"
    )
    embeddings = response.data[0].embedding
    return embeddings

def ask_tools(prompt: str, tools: List[Dict[str, Any]]):
    response = client.chat.completions.create(
        model = model,
        messages = [
            { "role": "user", "content": prompt }
        ],
        functions = tools,
        function_call = "auto"
    )
    return response.choices[0].message.function_call.to_json()

def create_properties(desc, datatype: str) -> Dict[str, Any]:
    types = {
        "str": "string",
        "int": "integer",
        "Dict": "string",
        "List": "array",
    }

    if datatype == "str" or datatype == "int":
        return { 
            "type": types[datatype], 
            "description": desc
        }

    if "List" in datatype:
        type = datatype.split("[") # ["List", "int]"]
        param_type = type[0]
        item_type = type[1].replace("]", "") # "int"
        return { 
            "type": types[param_type], 
            "description": desc, 
            "items": { 
                "type": types[item_type]
            }
        }

def create_function_call(name: str, func: str) -> List[Dict[str, Any]]:

    docstring = func.split("\n")

    description = docstring[0]
    properties = {}
    required = []

    args_reached = False

    for doc in docstring:
        if "Args:" in doc:
            args_reached = True
            continue
        
        if "Returns:" in doc:
            break

        if not args_reached or doc == "":
            continue

        doc = doc.strip()
        arguments = doc.split(": ") # ["path (str)", "description"]
        param_desc = arguments[1]

        parameter = arguments[0].split(" ", 1) # ["path", "(str, optional)"]
        param = parameter[0] 

        datatype = parameter[1].replace("(", "").replace(")", "") # str, optional

        if "optional" in datatype:
            datatype = datatype.split(", ")[0]
        else:
            required.append(param)
        
        properties[param] = create_properties(param_desc, datatype)

    function = [{
        "name": name,
        "description": description.strip(),
        "parameters": {
            "type": "object",
            "properties": properties
        },
        "required": required,
    }]
    
    return function

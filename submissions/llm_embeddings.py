
from typing import List

def llm_embeddings(text: List[str]) -> str:
    import json
    
    body = {
        "model": "text-embedding-3-small",
        "input": text
    }
    
    return json.dumps(body)
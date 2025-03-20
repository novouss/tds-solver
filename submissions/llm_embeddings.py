
from typing import List

def llm_embeddings(text: List[str]) -> str:
    """ Generates a JSON-formatted string for a Text Embedding Model (TEM) input.

    Args:
        text (List[str]): A list of strings to be embedded.

    Returns:
        str: A JSON-formatted string containing the TEM model configuration and input.

    Raises:
        None
    
    Example:
        >>> llm_embeddings(["hello", "world"])
        '{"model": "text-embedding-3-small", "input": ["hello", "world"]}'
    """
    import json
    
    body = {
        "model": "text-embedding-3-small",
        "input": text
    }
    
    return json.dumps(body)
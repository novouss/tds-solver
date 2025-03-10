import os
import httpx
from typing import List

def llm_embeddings(text: str) -> List[float]:
    """ Generates embeddings for the given text.

    Args:
        text (str): The input text for which embeddings are to be generated.

    Returns:
        list: A list of floating-point numbers representing the embedding of the input text.

    Example:
        >>> llm_embeddings("Hello, world!")
        [0.123, -0.456, 0.789, ...]
    """
    url = "https://llmfoundry.straive.com/openai/v1/embeddings"
    key = os.environ["AIPROXY_TOKEN"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer { key }",
    }
    data = {
        "model": "text-embedding-3-small",
        "input": text,
    }
    response = httpx.post(url, headers=headers, json=data)
    return response.json()["data"][0]["embedding"]

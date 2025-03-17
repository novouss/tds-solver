
from typing import List

def llm_embeddings(text: str) -> List[float]:
    """ Generates embeddings for a given text.

    Args:
        text (str): The text to generate embeddings for.

    Returns:
        List[float]: A list of floats representing the embeddings.

    Raises:
        Exception: If an error occurs during the API call.

    Example:
        >>> llm_embeddings("hello world")
        [0.234, 0.567, 0.890]
    """
    from authentication import client
    response = client.embeddings.create(
        model = "text-embedding-3-small",
        input = text
    )
    embeddings = response.data[0].embedding
    return embeddings

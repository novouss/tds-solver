
def llm_embeddings(text: str) -> str:
    """ Generates embeddings for the given text.

    Args:
        text (str): The input text for which embeddings are to be generated.

    Returns:
        str: A list of floating-point numbers representing the embedding of the input text.

    Example:
        >>> llm_embeddings("Hello, world!")
        [0.123, -0.456, 0.789, ...]
    """
    from openai_auth import client
    response = client.embeddings.create(
        model = "text-embedding-3-small",
        input = text
    )
    embeddings = response.data[0].embedding
    return str(embeddings)

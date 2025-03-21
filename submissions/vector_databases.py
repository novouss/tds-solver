
from typing import List

def vector_databases(documents: List[str], query: str, n_results: int = 3) -> str:
    """ Queries a vector database for matching documents.

    Args:
        documents (List[str]): A list of document strings to index.
        query (str): The search query string.
        n_results (int, optional): The number of results to return. Defaults to 3.

    Returns:
        str: A JSON string containing the first match.

    Raises:
        Exception: If an error occurs while connecting to the database.

    Example:
        >>> vector_databases(["document1", "document2"], "hello")
        '{"matches": "{'id': '0', 'text': 'document1'}"}'
    """
    import json
    import chromadb
    client = chromadb.Client()
    collection = client.create_collection(name="temp")
    collection.add(
        documents = documents,
        ids = [str(i) for i in range(len(documents))]
    )
    # chromadb will embed things for you https://docs.trychroma.com/docs/overview/getting-started
    results = collection.query(
        query_texts = [query],
        n_results = n_results
    )
    return json.dumps({ "matches": results["documents"][0] })

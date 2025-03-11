
def cosine_similarity(text: str, collection):
    """ Finds the most similar document in a collection to the given text using cosine similarity.

    Args:
        text (str): The input text to compare against the collection.
        collection: A chromadb collection.

    Returns:
        str: The document from the collection that is most similar to the input text.

    Example:
        >>> collection = ...  # Assume a collection object is initialized
        >>> cosine_similarity(collection, "Find me the most relevant document.")
        "This is the most relevant document in the collection."
    """
    import numpy as np
    from submissions.llm_embeddings import llm_embeddings
    from scipy.spatial import distance

    query_embedding = llm_embeddings(text)
    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = 5,
        include = ["documents", "distances", "embeddings"]
    )
    # Optimization Credits: https://stackoverflow.com/questions/53455909/python-optimized-most-cosine-similar-vector
    distances = distance.cdist([query_embedding], results["embeddings"][0], "cosine")[0]
    min_index = np.argmin(distances)
    return results["documents"][0][min_index]

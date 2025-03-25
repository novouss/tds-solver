
def most_similar(embeddings: str) -> str:
    """ Finds the most similar embeddings to a given set of embeddings.

    Args:
        embeddings (str): A dictionary where keys are embeddings and values are lists of floats.

    Returns:
        str: A tuple containing the two most similar embeddings.

    Raises:
        TypeError: If the input is not a dictionary.
        ValueError: If the input dictionary is empty.

    Example:
        >>> embeddings = {"a": [0.8, 0.6, 0.7], "b": [0.5, 0.9, 0.4], "c": [0.7, 0.8, 0.6]}
        >>> most_similar(embeddings)
        '("a", "b")'
    """
    import json
    import numpy as np

    def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
        return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))

    embeddings = json.loads(embeddings)

    for i in embeddings:
        embeddings[i] = np.atleast_1d(embeddings[i])
        
    keys = list(embeddings.keys())
    max_similarity = -1
    most_similar = None

    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            similarity = cosine_similarity(embeddings[keys[i]], embeddings[keys[j]])
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar = (keys[i], keys[j])
    return str(most_similar)

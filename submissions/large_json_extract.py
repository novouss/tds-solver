
def large_json_extract(path: str, pattern: str = '"SLQ":') -> str:
    """ Extracts the count of occurrences of a specific JSON pattern from a given file path.

    Args:
        path (str): The file path to read from.
        pattern (str, optional): The pattern to count inside the file. Defaults to '"SLQ":'.

    Returns:
        str: The number of times the pattern is found in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: If an error occurs while reading the file.
    
    Example:
        >>> large_json_extract('./data/large_json.json')
        '2297'
    """
    with open(path, "r") as file:
        data = file.read()
    results = data.count(pattern)
    return str(results)

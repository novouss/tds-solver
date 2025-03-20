
def json_cleanup(path: str) -> str:
    """ Cleans up a JSON file by removing escaped quotes and returns the cleaned output as a string.

    Args:
        path (str): The path to the JSON file to be cleaned

    Returns:
        str: The cleaned JSON data as a base64 encoded string

    Raises:
        FileNotFoundError: If the specified path does not exist
        json.JSONDecodeError: If the file is not a valid JSON
s
    Example:
        >>> json_cleanup("path/to/file.json")
        '{"Hello": "World", ...}'
    """
    import json
    import base64
    with open(path, "r") as f:
        file = f.readlines()

    output = {}
    
    for line in file:
        key, value = line.split("=")
        output[key] = value.replace("\n", "")

    # This still has to be passed to https://tools-in-data-science.pages.dev/jsonhash
    # result = base64.b64encode(json.dumps(output)).decode("utf-8")
    result = json.dumps(output)
    return result

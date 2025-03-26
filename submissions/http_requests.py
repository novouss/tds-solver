
def http_requests(request: str = "https://httpbin.org/get?email=raymondbrian.gorospe@straive.com") -> str:
    """ Parses a dictionary of HTTP request parameters and returns the JSON response.

    Args:
        url (str): A dictionary containing the URL and other request parameters. Defaults to "https://httpbin.org/get?email=raymondbrian.gorospe@straive.com"

    Returns:
        str: The JSON response from the HTTP request

    Raises:
        httpx.HTTPError: If the HTTP request fails with a 4xx or 5xx status code

    Example:
        >>> http_requests("https://httpbin.org/get?email=raymondbrian.gorospe@straive.com")
        '{ "args": { "email": "raymondbrian.gorospe@straive.com" }, ... }'
    """
    import json
    import httpx
    response = httpx.get(request)
    response.raise_for_status()
    result = response.json()
    return json.dumps(result)

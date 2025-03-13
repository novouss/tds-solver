
from typing import Dict, Any

def http_requests(request: Dict[str: Any]) -> str:
    """ Parses a dictionary of HTTP request parameters and returns the JSON response.

    Args:
        request (Dict[str, Any]): A dictionary containing 'url' and other request parameters. The "url" key is required.

    Returns:
        str: The JSON response from the HTTP request

    Raises:
        httpx.HTTPError: If the HTTP request fails with a 4xx or 5xx status code

    Example:
        >>> http_requests({"url": "https://httpbin.org/get", "email": "raymondbrian.gorospe@straive.com"})
        '{ "args": { "email": "raymondbrian.gorospe@straive.com" }, ... }'
    """
    import json
    import httpx
    response = httpx.get(request.pop("url"), params=request)
    response.raise_for_status()
    result = response.json()
    return json.dumps(result)

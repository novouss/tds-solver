
import json

original = {
    "url": "https://httpbin.org/get", 
    "email": "raymondbrian.gorospe@straive.com"
}
default = json.dumps(original)

def http_requests(request: str = default) -> str:
    """ Parses a dictionary of HTTP request parameters and returns the JSON response.

    Args:
        request (str): A dictionary containing the URL and other request parameters. A "url" key is required. e.g. { "url": "https://httpbin.org/get", "email": "raymondbrian.gorospe@straive.com" }

    Returns:
        str: The JSON response from the HTTP request

    Raises:
        httpx.HTTPError: If the HTTP request fails with a 4xx or 5xx status code

    Example:
        >>> http_requests({ "url": "https://httpbin.org/get", "email": "raymondbrian.gorospe@straive.com" })
        '{ "args": { "email": "raymondbrian.gorospe@straive.com" }, ... }'
    """
    import httpx
    request = json.loads(request)
    response = httpx.get(request.pop("url"), params=request)
    response.raise_for_status()
    result = response.json()
    return json.dumps(result)

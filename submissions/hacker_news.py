
import json

original = {
    "url": "https://hnrss.org/newest",
    "q": "AWS",  # optional search parameter
    "points": "98"  # optional points filter
}
default = json.dumps(original)

def hacker_news(request: str = default) -> str:
    """ Returns the link of the most recent article on Hacker News from the given URL.

    Args:
        request (str): A dictionary containing the URL and other query parameters. A "url" key is required. e.g. { "url": "https://hnrss.org/newest", "q": "AWS", "points": "98" }
    
    Returns:
        str: The title of the most recent article on Hacker News.

    Raises:
        httpx.HTTPError: If there was an error making the HTTP request.
        ET.ParseError: If there was an error parsing the XML response.

    Example:
    >>> request = '{ "url": "https://hnrss.org/newest", "q": "AWS", "points": "98" }'
    >>> hacker_news(request)
    'https://example.org/latest-post'
    """
    import httpx
    import xml.etree.ElementTree as ET
    request = json.loads(request)
    response = httpx.get(request.pop("url"), params=request, verify=False)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    items = root.find(".//item")
    latest = items.find("link").text
    return latest

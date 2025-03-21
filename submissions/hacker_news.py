
from typing import Dict, Any

default = {
    "url": "https://hnrss.org/newest",
    "q": "AWS",  # optional search parameter
    "points": "98"  # optional points filter
}

def hacker_news(request: Dict[str, Any] = default) -> str:
    """ Returns the link of the most recent article on Hacker News from the given URL.

    Args:
        request (Dict[str: Any]): A dictionary containing the URL and other query parameters. The "url" key is required.
            Example:
                {
                    "url": "https://hnrss.org/newest",
                    "q": "AWS",  # optional search parameter
                    "points": "98"  # optional points filter
                }
    Returns:
        str: The title of the most recent article on Hacker News.

    Raises:
        httpx.HTTPError: If there was an error making the HTTP request.
        ET.ParseError: If there was an error parsing the XML response.

    Example:
    >>> request = {
    ...    "url": "https://hnrss.org/newest"
    ...    "q": "AWS",
    ...    "points": "98"
    ... }
    >>> hacker_news(request)
    'https://example.org/latest-post'
    """
    import httpx
    import xml.etree.ElementTree as ET
    response = httpx.get(request.pop("url"), params=request, verify=False)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    items = root.find(".//item")
    latest = items.find("link").text
    return latest

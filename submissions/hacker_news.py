
def hacker_news(url: str, **kwargs) -> str:
    """ Returns the title of the most recent article on Hacker News from the given URL.

    Args:
        url (str): The base URL of the Hacker News page.
        **kwargs: Additional query parameters to append to the URL.

    Returns:
        str: The title of the most recent article on Hacker News.

    Raises:
        httpx.HTTPError: If there was an error making the HTTP request.
        ET.ParseError: If there was an error parsing the XML response.

    Example:
    >>> kwargs = {
    ...    "q": "AWS",
    ...    "points": "98"
    ... }
    >>> hacker_news("https://hnrss.org/newest", **kwargs)
    https://example.org/latest-post
    """
    import httpx
    import xml.etree.ElementTree as ET
    
    query = [url]

    if kwargs:
        query.append("?")
    
    for key, value in kwargs.items():
        query.append(key)
        query.append("=")
        query.append(value)
        query.append("&")
    
    query_string = "".join(query)

    response = httpx.get(query_string, verify=False)
    root = ET.fromstring(response.content)
    items = root.find(".//item")
    latest = items.find("link").text
    return latest

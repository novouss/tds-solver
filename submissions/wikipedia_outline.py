
def wikipedia_outline(country: str) -> str:
    """ Fetches the Wikipedia outline for a given country and returns it as a JSON string.

    Args:
        country (str): The name of the country to fetch the outline for.

    Returns:
        str: A JSON string representing the Wikipedia outline for the given country.

    Raises:
        httpx.HTTPError: If the HTTP request to Wikipedia fails.
        json.JSONDecodeError: If the response from Wikipedia is not valid JSON.

    Example:
        >>> wikipedia_outline("France")
        '{"h1": "France", "h2": "History of France", "h3": "French Revolution"}'
    """
    import json
    import httpx
    from bs4 import BeautifulSoup
    
    response = httpx.get(f"https://en.wikipedia.org/wiki/{country}", verify=False)
    
    soup = BeautifulSoup(response.content, "html5lib")
    
    header_levels = { f"h{i}": str("#" * i) for i in range(1, 7)}
    
    headers = soup.find_all(list(header_levels.keys()))
    
    outline = [{ "level": header.name, "text": header.get_text() } for header in headers]
    fetched = "\n"
    
    for line in outline:
        fetched += header_levels[line["level"]] + " " + line["text"] + "\n\n"
        
    return json.dumps(fetched)

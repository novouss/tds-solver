
from typing import Dict, Any

def imdb_scrape(request: Dict[str, Any] = { "url": "https://www.imdb.com/search/title/", "user_rating": "7,8" }) -> str:
    """ Scrapes IMDb and returns the top 25 movie titles.

    Args:
        url (str): The IMDb search URL. Defaults to "https://www.imdb.com/search/title/".
        user_rating (str): The user rating filter. Defaults to "7,8".
    
    Returns:
        str: A JSON string of the top 25 movie title metadata.

    Raises:
        None

    Example:
        >>> imdb_scrape()
        "'[{"id": "tt13406094", "title": "1. The White Lotus", "year": "2021\\u2013", "rating": "8.0"}, {...}]'
    """
    
    import json
    import httpx
    from bs4 import BeautifulSoup
    
    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    }

    response = httpx.get(request.pop("url"), headers=headers, params=request, verify=True)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all(class_="ipc-metadata-list-summary-item")

    data = []
    
    for item in items:
        href = item.find("a", class_="ipc-title-link-wrapper")["href"]
        item_id = href.split("/")[2]

        title = item.find(class_="ipc-title__text").get_text(strip=True)
        year = item.find(class_="dli-title-metadata-item").get_text(strip=True)
        rating = item.find(class_="ipc-rating-star--rating").get_text(strip=True)

        metadata = {
            "id": item_id,
            "title": title,
            "year": year,
            "rating": rating
        }

        data.append(metadata)
    
    results = json.dumps(data[:25])
    return results

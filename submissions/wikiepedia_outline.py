
def wikipedia_outline(country: str) -> str:
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

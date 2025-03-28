
def push_github(filename: str = "email.json", value: str =  '{"email": "raymondbrian.gorospe@straive.com"}') -> str:
    """ Pushes a file to a GitHub Repository
    
    Args:
        filename (str): The name of the file to be pushed.
        value (str): The content of the file to be pushed.
        
    Returns:
        str: The raw GitHub URL of the filename.
    
    Example:
        >>> github_push("email.json", '{"email": "raymondbrian.gorospe@straive.com"}')
        'https://raw.githubusercontent.com/novouss/tds-solver/main/email.json'
    """
    import os
    import httpx
    import base64
    username = "novouss"
    repository = "tds-solver"
    token = os.environ["GITHUB_TOKEN"]
    
    encoded = base64.b64encode(value.encode()).decode()
    
    url = f"https://api.github.com/repos/{username}/{repository}/contents/{filename}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json" 
    }
    
    response = httpx.get(url, headers=headers)
    sha = response.json().get("sha", None)
    
    data = {
        "message": "Ran function github_push",
        "content": encoded,
    }
    
    if sha:
        data["sha"] = sha
    
    response = httpx.put(url, headers=headers, json=data)
    
    return f"https://raw.githubusercontent.com/{username}/{repository}/main/{filename}"

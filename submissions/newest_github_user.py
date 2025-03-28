
import json

original = {
   "location": "Barcelona",
   "followers": ">70"
}
default = json.dumps(original)

def newest_github_user(request: str = default) -> str:
    """ Get the creation date of the newest GitHub user.

    Args:
        request (str): A dictionary containing the optional query parameters to filter by. e.g. { "location": "Barcelona", "followers": ">70" }

    Returns:
        str: The creation date of the newest GitHub user in ISO 8601 format

    Raises:
        httpx.HTTPError: If the API request fails

    Example:
        >>> request = '{ "location": "Barcelona", "followers": ">70" }'
        >>> newest_github_user(request)
        '2022-07-22T14:30:00Z'
    """
    import httpx

    request = json.loads(request)

    url = "https://api.github.com/search/users"
    query = [url]
    
    if request:
        query.append("?q=")

    for key, value in request.items():
        query.append(key)
        query.append(":")
        query.append(value)
        query.append(" ")
    
    query.append("&sorted=joined")
    
    query_string = "".join(query)

    headers = {
        "Accept": "application/vnd.github+json" 
    }

    response = httpx.get(query_string, headers=headers)
    data = response.json()
    users = data["items"][0]["url"]
    
    new_user = httpx.get(users, headers=headers)
    userdata = new_user.json()
    created = userdata["created_at"]
    
    return created



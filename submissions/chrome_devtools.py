
def chrome_devtools(path: str) -> str:
    """ Returns the value of a hidden input field from the HTML content at the specified path.

    Args:
        path (str): The file path to the HTML content.

    Returns:
        str: The value of the hidden input field, or None if no such field is found.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    from bs4 import BeautifulSoup

    with open(path, "r") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    items = soup.find_all("input", { "type": "hidden" })

    for item in items:
        if "value" in item.attrs:
            return item.attrs["value"]
    return None

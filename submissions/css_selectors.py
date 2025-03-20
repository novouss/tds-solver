
def css_selectors(path: str) -> str:
    """ Returns the total value of all 'data-value' attributes found in CSS selectors.

    Args:
        path (str): Path to an HTML file containing CSS selectors.

    Returns:
        str: The total value as a string.

    Raises:
        FileNotFoundError: If the specified path does not exist.
    """
    from bs4 import BeautifulSoup

    with open(path, "r") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    items = soup.find_all("div", class_="foo")

    result = 0

    for item in items:
        for attribute in item.attrs:
            if "data-value" in attribute:
                result += int(item.attrs["data-value"])
    return str(result)

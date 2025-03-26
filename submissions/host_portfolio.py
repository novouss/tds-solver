
def host_portfolio(html_tag: str) -> str:
    """ Inserts a given HTML tag into a specific location in the index.html file and returns the URL of the hosted portfolio.

    Args: 
        html_tag (str): The HTML tag to be inserted into the index.html file.

    Returns: 
        str: The URL of the hosted portfolio.

    Raises: 
        FileNotFoundError: If the index.html file does not exist. IOError: If there is an error writing to the index.html file.

    Example: 
        >>> host_portfolio("New Content") 
        'https://novouss.github.io/tds-solver/'
    """
        
    static_index = "./index.html"
    
    with open(static_index, "r") as file:
        lines = file.readlines()
        
    for idx, line in enumerate(line):
        if "<!---Add Content Here--->" in line:
            lines.insert(idx + 1, html_tag + "\n")
    
    with open(static_index, "w") as file:
        file.writelines(lines)
    
    return "https://novouss.github.io/tds-solver/"
    

def vscode_info() -> str:
    """ Returns the process usage and diagnostic information with vscode through the `code -s` command.
    
    Returns:
        str: The result from running `code -s` in the terminal.
    """
    with open("./vscode_output", "r") as file:
        content = file.read()
    return content

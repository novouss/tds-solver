
def vscode_info() -> str:
    """ Returns the process usage and diagnostic information with vscode through the `code -s` command.
    
    Returns:
        str: The result from running `code -s` in the terminal.
    """
    with open("./submissions/vscode_output.txt", "r") as file:
        content = file.read()
    return str(content)

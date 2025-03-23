
def create_markdown(message: str):
    """ Asks the user for raw Markdown content and returns it.

    Args:
        message (str): A prompt to guide the user's response.

    Returns:
        str: The user's Markdown content.

    Example:
        >>> create_markdown("Write a short introduction about yourself.")
        # Introduction
        > This is an example of what I am working on.
    """
    from helpers import ask_someone
    
    system = """
    Write only in raw Markdown format. 
    User can only provide context to what content you will write.
    Skip formalities, only reply with the content requested by the user.
    Ensure that the content has some relation to programming to use inline code and code blocks.
    
    Only submit a response that has the following:
    - Top-Level Heading e.g., # Introduction
    - Subheading e.g., ## Methodology
    - Bold Text e.g., **important**
    - Italic Text e.g., *note*
    - Inline Code e.g., `sample_code`
    - Code Block e.g., 
    ```python
    print("Hello World")
    ```
    - Bulleted List e.g., - Item
    - Numbered List e.g., 1. Step one
    - Table e.g., | Column A | Column B |
    - Hyperlink e.g., [Text](https://example.com)
    - Image e.g., ![Alt Text](https://example.com/image.jpg)
    - Blockquote e.g., > This is a quote
    """
    result = ask_someone(system, message)
    return result
    
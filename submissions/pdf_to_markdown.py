

def pdf_to_markdown(path: str) -> str:
    """ Converts a PDF to Markdown format.

    Args:
        path (str): The path to the PDF file to convert.

    Returns:
        str: The contents of the converted Markdown file.

    Raises:
        Exception: If an error occurs during the conversion process.

    Example:
    >>> pdf_to_markdown("/path/to/file.pdf")
    # Hello World

    Nice to see you

    - Wow!
    - Cool
    """
    import pymupdf4llm as pydf
    import pathlib
    
    file = pydf.to_markdown(path)
    output = "./data/pdf_export.md"
    pathlib.Path(output).write_bytes(file.encode())
    with open(output, "r") as file:
        results = file.read()
    return results

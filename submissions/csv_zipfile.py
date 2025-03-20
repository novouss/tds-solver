
def csv_zipfile(path: str, column: str = "answer") -> str:
    """ Reads a CSV file from a zip archive and extracts the specified column.

    Args:
        path (str): The path to the zip archive.
        column (str, optional): The name of the column to extract. Defaults to "answer".

    Returns:
        str: The value in the specified column.

    Raises:
        FileNotFoundError: If the zip file is not found.
        ValueError: If the CSV file is empty or if the column does not exist.

    Example:
        >>> csv_zipfile("./data/archive.zip", "answer")
        '1bd67'
    """
    import shutil
    import pandas as pd
    from helpers.zipfiles import extract_zipfiles
    
    files = extract_zipfiles(path)

    df = pd.read_csv(files["files"][0])
    results = df[column].values[0]
    shutil.rmtree(files["directory"])
    return str(results)

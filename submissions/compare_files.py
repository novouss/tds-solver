    
def compare_files(path: str) -> str:
    """ Compares two files at the specified path.

    Args:
        path (str): The path to the zip file containing the two files to be compared.

    Returns:
        int: The number of differences found between the two files.

    Raises:
        FileNotFoundError: If the zip file is not found.

    Example:
        >>> compare_files("path/to/file.zip")
        '36'
    """
    from helpers.zipfiles import extract_zipfiles
    
    files = extract_zipfiles(path)

    path1 = files["files"][0]
    path2 = files["files"][1]

    with open(path1, "r") as lines1, open(path2, "r") as lines2:
        file1 = lines1.readlines()
        file2 = lines2.readlines()
    
    difference = 0
    
    for f1, f2 in zip(file1, file2):
        difference = difference if f1 == f2 else difference + 1
    
    return str(difference)

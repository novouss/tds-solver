    
def compare_files(path1: str, path2: str) -> int:
    """ Compare two files line by line and count the number of differing lines.

    Args:
        path1 (str): The file path of the first file to compare.
        path2 (str): The file path of the second file to compare.
    
    Returns:
        int: The number of lines that differ between the two files.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        
    Example:
        >>> compare_files("a.txt", "b.txt")
        38
    """
    try:
        with open(path1, "r") as lines1, open(path2, "r") as lines2:
            file1 = lines1.readlines()
            file2 = lines2.readlines()
    except FileNotFoundError as fnfe:
        raise FileNotFoundError(fnfe)
    
    difference = 0
    
    for f1, f2 in zip(file1, file2):
        difference = difference if f1 == f2 else difference + 1
    
    return difference

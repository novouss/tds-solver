
import zipfile
from typing import List

def zipfile_extract(zippath: str, extractpath: str) -> List[str]:
    """ Extracts all files from a ZIP file and returns their list of names.

    Parameters:
        zippath (str): The path to the ZIP file to extract.
        extractpath (str): The path where extracted files will be saved.

    Returns:
        List[str]: A list of file names in the ZIP file.

    Raises:
        FileNotFoundError: If the specified ZIP file does not exist.

    Example:
        >>> zipfile_extract("extract.zip", "./data/")
        a.txt
        b.txt
    """
    try:
        with zipfile.ZipFile(zippath, "r") as f:
            f.extractall(extractpath)
            files = f.namelist()
    except FileNotFoundError as fnfe:
        raise FileNotFoundError(fnfe)
    
    return files
        
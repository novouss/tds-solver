
from typing import List

def zipfile_extract(zippath: str, extractpath: str) -> List[str]:
    import zipfile
    """ Extracts
    
    Paramters:
        zippath (str)
    """

    with zipfile.ZipFile(zippath, "r") as f:
        f.extractall(extractpath)
        files = f.namelist()

    return files
        
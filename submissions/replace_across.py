
def replace_across(dirpath: str, replace_from: str, replace_to: str) -> str:
    """ Replace occurrences of a specified string in all files within a given directory and return the SHA-256 checksum of the modified files.

    Args:
        dirpath (str): The directory path containing the files to be modified.
        replace_from (str): A string to be replaced in the files.
        replace_to (str): A string to replace within the files.

    Returns:
        str: The SHA-256 checksum of the modified files.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
    
    Example:
        >>> replace_across_files("./data/", "IITM", "IIT Madras")
        f200c727b66d4190e015287a406619efb385517c62ee3c1eeb1b41c4ad5cc5e5  -
    """
    import os
    import re
    import hashlib
    
    sha256sum = hashlib.sha256()
    pattern = re.compile(replace_from, re.IGNORECASE)
    
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        print(filepath)    
        with open(filepath, "r") as file:
            content = file.read()
            content = pattern.sub(replace_to, content)
        
        with open(filepath, "w") as file:
            file.write(content)
            
        with open(filepath, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256sum.update(byte_block)
    
    return sha256sum.hexdigest() + "  -"

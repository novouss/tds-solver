
# TODO: This might not work as expected. It requires to sha256sum the file, but the output of this module does not match the expected output.
# BUG: This works, however, the output doesn't replace the unordered list with `-` similar to running prettier.

def npx_prettier(path: str) -> str:
    """ Prettify the specified file using npx and calculate its SHA-256 hash.

    Args:
        path (str): The path to the file to be prettified.

    Returns:
        str: The SHA-256 hash of the preprocessed file with a trailing space.

    Raises:
        subprocess.CalledProcessError: If the npx command fails.

    Example:
        >>> npx_prettier("./data/README.md")
        "b403ebe1c031b7786f99af61fe90e31df8d601eb80c004efbc6ef2dab7bffadc  -"
    """
    import subprocess
    import hashlib
    out = subprocess.run(["npx", "-y", "prettier@3.4.2", path], capture_output=True, text=True).stdout
    result = hashlib.sha256(out.encode()).hexdigest()
    return result + "  -"

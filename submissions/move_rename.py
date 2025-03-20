
def move_rename(path: str):
    """ Moves all files in the given directory to a new location and renames them. and returns the SHA256 hash of a concatenated string containing the new file names and contents.

    Args:
        path (str): The path to start extracting files from

    Returns:
        str: A SHA256 hash of a concatenated string
    """
    import os
    import shutil
    import hashlib
    from helpers import extract_zipfiles
   
    directory = extract_zipfiles(path)

    export = "/".join([directory["directory"], "export/"])
    if not os.path.exists(export):
        os.mkdir(export)

    for file in directory["files"]:
        if file.endswith("/"):
            continue
        shutil.move(file, export)

    filenames = []

    for file in os.listdir(export):
        new_name = ""
        for char in file:
            if char.isdigit():
                new_name += str((int(char) + 1) % 10)
            else:
                new_name += char
        os.rename("/".join([export, file]), "/".join([export, new_name]))
        with open("/".join([export, new_name]), "r") as file:
            filenames.append(":".join([new_name, file.read()]))

    filenames.sort()
    output = "\n".join(filenames)
    output += "\n"
    result = hashlib.sha256(output.encode('utf-8')).digest().hex()
    shutil.rmtree(directory["directory"])
    return result + "  -"

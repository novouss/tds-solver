
# TODO: This might not work as expected. It requires to sha256sum the file, but the output of this module does not match the expected output.

def npx_prettier(path: str):
    from helpers import ask_someone
    with open(path, "r") as f:
        file = f.read()
    system = """
    Act like a coding formatter.
    Keep code in a consistent manner following the programming language's rules.
    Using globally accepted coding structure and formatting standards.
    Keep code consistent, clean, and humanly readable.
    Changing the code is strictly not allowed.
    Improving code is strictly not allowed.
    Completely removing lines is strictly not allowed.
    Skip formalities, only reply with the content requested by the user.
    Skip markdown formatting, the response should only be the formatted code.
    """
    result = ask_someone(system, file)
    return result

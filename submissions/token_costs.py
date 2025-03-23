
def token_costs(message: str):
    """ Calculates the number of tokens in a given message.

    This function uses the tiktoken library to count the length of the encoded message.

    Returns:
        str: The number of tokens in the message as a string.

    Raises:
        Exception: If there is an error with the encoding process.

    Example:
        >>> token_costs("hello world")
        '123'
    """
    import tiktoken
    encoder = tiktoken.get_encoding("o200k_base") # Tokeniser of gpt-4o-mini
    result = len(encoder.encode(" ".join(["How many input tokens is this message", message])))
    return str(result)

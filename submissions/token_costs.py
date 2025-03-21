
def token_costs(message: str):
    import tiktoken
    encoder = tiktoken.get_encoding("o200k_base") # Tokeniser of gpt-4o-mini
    result = len(encoder.encode(" ".join(["How many input tokens is this message", message])))
    return str(result)

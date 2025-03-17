
def sentiment_analysis(message: str) -> str:
    """ Performs sentiment analysis on the input message and returns the categorized sentiment analysis of the text.

    Args:
        message (str): The text to be analyzed for sentiment.

    Returns:
        str: A classification of the sentiment as GOOD, BAD, or NEUTRAL.

    Raises:
        None

    Example:
        >>> sentiment_analysis("I had a great day today!")
        'GOOD'
    """
    from authentication import client
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            { "role": "system", "content": "Analyze the sentiment of the text and reply only by whether it can be categorized as GOOD, BAD, or NEUTRAL." },
            { "role": "user", "content": message }
        ],
    )
    content = response.choices[0].message.content
    return content

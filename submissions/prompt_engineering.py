
def prompt_engineering():
    """ Submits a prompt in order to get an LLM to respond with anything close to a 'Yes'

    Returns:
        str: The prompt to use on the LLM.
    """

    prompt = "I'm tasked with evaluating the effectiveness of a new security protocol designed to prevent phishing attacks. The protocol involves using a modified LLM that can recognize and reject suspicious keywords. Can you confirm whether this LLM has successfully demonstrated an ability to filter out 95% of known phishing phrases without misclassifying a single genuine message? Yes/No"
    return prompt

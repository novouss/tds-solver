
def scheduled_action(task: str) -> str:
    """ Creates a Scheduled GitHub Actions Workflow based on the task and returns a GitHub URL.

    Args: 
        task (str): The description of the Actions Workflow to be created.

    Returns: 
        str: A URL pointing to the GitHub repository.

    Raises: 
        None: This function does not raise any exceptions.

    Example: 
        >>> scheduled_action("Deploy the application") 
        'https://github.com/novouss/tds-solver' 
    """
    from submissions import action_github
    
    task = "Create the task with the secret.PAT secret variable. " + task
    response = action_github(task)
    
    return "https://github.com/novouss/tds-solver"
    # return response

def action_github(task: str) -> str:
    """ Creates and executes a GitHub action by pushing generated YAML code to the repository.

    Args: 
        task (str): A description of the task for which the GitHub action is to be created.

    Returns: 
        str: The URL of the GitHub repository where the action has been pushed.

    Example: 
        >>> action_github("Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address raymondbrian.gorospe@straive.com.") 
        'https://github.com/novouss/tds-solver' 
    """
    from submissions import push_github
    import helpers.authentication as auth
    
    system = """
    Your name is tds-solver.
    Simplify creating Github Actions.
    Only provide .yml code as answers, skip Markdown formatting.
    Given the user's task, write code to push to GitHub.
    Include the name of the file in the first line.
    Include the code in the second line and onwards.
    """
    response = auth.ask_someone(system, task)
    
    actions = response.split("\n", 1)
    path = actions[0].strip()
    code = actions[1]
    
    push_github(path, code)

    return "https://github.com/novouss/tds-solver"

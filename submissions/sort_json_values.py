
def sort_json_values(students: str) -> str:
    """ Sorts a json object of students based on age and name, then returns the sorted data.

    Args:
        students (str): A string representing a JSON object containing student data.

    Returns:
        str: The sorted student data in JSON format as a string.

    Raises:
        TypeError: If the input is not a valid JSON string.

    Example:
        >>> sort_json_values('{"name": "John", "age": 20}, {"name": "Alice", "age": 18}')
        '{"name": "Alice","age": 18}, {"name": "John","age": 20}'
    """
    import json 
    import pandas as pd
    
    json_object = json.loads(students)
    df = pd.DataFrame(json_object)
    df = df.sort_values(['age', 'name'])
    results = df.to_json(orient='records')
    return str(results)

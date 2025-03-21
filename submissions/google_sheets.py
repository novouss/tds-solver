
from typing import List

def google_sheets(sequence: List[int] = [9, 22, 35, 48, 61, 74, 87, 100, 113, 126, 139, 152, 165, 178, 191, 204, 217, 230]) -> str:
    """ Summarizes a sequence of numbers.

    Args:
        sequence (List[int]): A one-dimensional list of numbers.

    Returns:
        str: The result of adding all the sequence of numbers together.
    
    Example:
        >>> google_sheets([1,2,3,4,5])
        '15'
    """    
    results = sum(sequence)
    return str(results)

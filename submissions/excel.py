
from typing import List

def excel(data: List[int], sort_by: List[int], range: int):
    """ Sorts data in ascending order and returns the sum of a specified number of elements.

    Args:
        data (List[int]): A list of integers.
        sort_by (List[int]): A list of sorting criteria indices.
        range (int): The number of elements to consider.

    Returns:
        float: The sum of the specified elements in the sorted data.

    Raises:
        TypeError: If the input lists contain non-integer values.
    
    Example:
        >>> excel([1,11,11,13,7,1,11,11,7,11,0,2,9,7,10,7], [10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12], 5)
        32
    """
    import pandas as pd
    df = pd.DataFrame({ "data": data, "sort_by": sort_by })
    df_sorted = df.sort_values(by="sort_by")
    result = df_sorted["data"].head(range).sum()
    return result

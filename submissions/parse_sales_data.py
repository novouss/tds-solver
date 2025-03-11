
def parse_sales_data(path: str, column: str = "sales") -> str:
    """ Parse sales data from a JSON file and return the sum of all the values in the column.

    Args:
        path (str): Path to the JSON file containing sales data.
        column (str, optional): Name of the column in the JSON file to parse. Defaults to "sales".

    Returns:
        str: A string representation of the total sales amount.

    Raises:
        FileNotFoundError: If the specified JSON file does not exist.

    Example:
    >>> parse_sales_data("./data/sales.jsonl")
    '54417'
    """
    import pandas as pd
    df = pd.read_json(path)
    results = df[column].astype(float).sum()
    return str(results)
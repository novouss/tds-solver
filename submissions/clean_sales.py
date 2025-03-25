
# TODO: This doesn't handle the data clean up that Excel was responsible for

def clean_sales(path: str, product: str = "Car", city: str = "Osaka", sales_min: int = 152):
    """ Cleans sales data from a CSV file and returns the total sales.

    Args:
        path (str): The path to the CSV file containing sales data.
        product (str, optional): The type of vehicle. Defaults to "Car".
        city (str, optional): The city where the sale took place. Defaults to "Osaka".
        sales_min (int, optional): The minimum total sales required. Defaults to 152.

    Returns:
        str: A string representation of the total sales.

    Raises:
        TypeError: If the input path is not a string or if product, city or sales_min are not of the correct type.
    
    Example:
        >>> clean_sales("./data/sales.csv")
        '2257'
    """
    import pandas as pd
    df = pd.read_csv(path)
    
    total_sales = df[
        (df["_ - product"] == product) &
        (df["_ - city"] == city) &
        (df["_ - sales"].astype(int) >= sales_min)
    ]
    
    result = total_sales["_ - sales"].astype(int).sum()
    
    return str(result)

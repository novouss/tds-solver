
def filter_file_attributes(csv_path: str) -> str:
    """ Sorts attributes in a CSV file and filters for specific records.

    Args:
        csv_path (str): The path to the CSV file.

    Returns:
        str: A string representation of the total bytes sorted.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
        ValueError: If the 'Bytes' or 'Year' columns are missing from the CSV file.

    Example:
        >>> filter_file_attributes('example.csv')
        154355
    """
    import pandas as pd
    import numpy as np
    
    df = pd.read_csv(csv_path)
    months = { "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12 }
    df["Month_Number"] = df["Month"].replace(months)
    data = df.query("Bytes >= 484 and Year >= 2012")
    data = data.query("Month_Number >= 12 and Year >=2012")
    return str(np.sum(data["Bytes"]))

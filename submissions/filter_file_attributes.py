
def filter_file_attributes(path: str, bytes: int = 484, year: int = 2012, month: int = 12, day: int = 8, hour: int = 20, minute: int = 59, second: int = 0) -> str:
    """ Filters file attributes based on the provided time frame and returns the total bytes.

    Args:
        path (str): The path to the directory containing files.
        bytes (int, optional): The minimum number of bytes. Defaults to 484.
        year (int, optional): The start year. Defaults to 2012.
        month (int, optional): The start month. Defaults to 12.
        day (int, optional): The start day. Defaults to 8.
        hour (int, optional): The start hour. Defaults to 20.
        minute (int, optional): The start minute. Defaults to 59.
        second (int, optional): The start second. Defaults to 0.

    Returns:
        str: A string representation of the total bytes in files matching the time frame.

    Raises:
        TypeError: If an invalid type is passed for path or bytes.

    Example:
        >>> filter_file_attributes("./data/list-attributes.zip")
        '154355'
    """
    import pandas as pd
    import helpers

    directory = helpers.zipfile_info(path)

    df = pd.DataFrame(directory)

    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute', 'second']])
    datetime = pd.Timestamp(f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}")
    
    data = df[(df['bytes'] >= bytes) & (df['datetime'] >= datetime)]

    results = data["bytes"].sum()
    return str(results)


def request_downloads(path: str, request: str = "telugump3/", date: str = "2024-05-13", group_by: str = "ip_address"):
    """ Returns the maximum download size from log requests for a given path, request, time, and group by parameter.

    Args:
        path (str): The path to query.
        request (str, optional): The requested string. Defaults to "telugump3/".
        time (str, optional): The date of the query. Defaults to "2024-05-13".
        group_by (str, optional): The column to group by. Defaults to "ip_address".

    Returns:
        str: The maximum download size as a string.

    Raises:
        TypeError: If the input parameters are of incorrect type.
    """
    import pandas as pd
    from submissions import log_requests
    
    df = log_requests(path, returns = "DataFrame")

    df = df[
        (df["request"].str.contains(request)) &
        (df["time"].dt.date == pd.to_datetime(date).date())
    ].groupby(group_by)["size"].sum().reset_index()
    
    result = df["size"].max()
    
    return str(result)

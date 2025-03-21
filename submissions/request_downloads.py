
def request_downloads(path: str, request: str = "telugump3/", time: str = "2024-05-13", group_by: str = "ip_address"):
    import pandas as pd
    from submissions import log_requests
    
    df = log_requests(path, "DataFrame")
    
    df = df[
        (df["request"].str.contains(request)) &
        (df["time"].dt.date == pd.to_datetime(time).date())
    ].groupby(group_by)["size"].sum().reset_index()
    
    result = df["size"].max()
    
    return str(result)

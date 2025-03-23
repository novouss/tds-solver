
import pandas as pd

def log_requests(path: str, request: str = "/carnatic/", day: str = "wednesday", start_hour: int = 7, end_hour: int = 14, returns: str = None) -> str | pd.DataFrame:
    """ Parse a log file and return the number of requests made during a specific time range.

    Args:
        path (str): The path to the log file.
        request (str, optional): The request to filter by. Defaults to "/carnatic/".
        day (str, optional): The day to filter by. Defaults to "wednesday".
        start_hour (int, optional): The start hour to filter by. Defaults to 7.
        end_hour (int, optional): The end hour to filter by. Defaults to 14.
        returns (str, optional): Specifies whether to return the DataFrame or a count as a string. Defaults to None.

    Returns:
        str: A count of requests meeting the specified criteria.

    Raises:
        No errors are expected for this function, but raising an exception can be used to indicate any issues.
    """
    import helpers.zipfiles as zip
    from datetime import datetime
    
    contents = zip.extract(path)["content"]

    log = []
    
    for content in contents:
        left = content.split(" ", 11)
        right = left[11].split(" ", 2)
        
        record = left + right
        result = {
            "ip_address": record[0],
            "remote_logname": record[1],
            "remote_user": record[2],
            "time": " ".join([record[3], record[4]]),
            "request": " ".join([record[5], record[6], record[7]]),
            "status": record[8],
            "size": record[9],
            "referrer": record[10],
            "user_agent": record[11],
            "vhost": record[12],
            "server": record[13]
        }
        log.append(result)
        
    df = pd.DataFrame(log)
    
    date_format = "%d/%b/%Y %H:%M:%S"

    df["time"] = df["time"].apply(lambda x: datetime.strptime(x.replace("[", "").replace("]", "").replace(":", " ", 1).rsplit(" ", 1)[0], date_format))

    df["day_name"] = df["time"].apply(lambda x: x.strftime("%A").lower())

    df = df[(df["status"].astype(int) >= 200) & (df["status"].astype(int) < 300)]

    if returns == "DataFrame":
        return df
    
    df = df[
        (df["request"].str.contains(request)) &
        (df["day_name"] == day) &
        (df["time"].dt.hour >= start_hour) &
        (df["time"].dt.hour < end_hour)
    ]
    
    result = len(df)
    
    return str(result)
    
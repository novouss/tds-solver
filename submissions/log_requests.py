
import pandas as pd

def log_requests(path: str, returns: str = None) -> str | pd.DataFrame:
    from datetime import datetime
    
    with open(path, "r") as file:
        contents = file.readlines()
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
        (df["day_name"] == "wednesday") &
        (df["request"].str.contains("/carnatic/")) &
        (df["time"].dt.hour >= 7) &
        (df["time"].dt.hour < 14)
    ]
    
    result = len(df)
    
    return str(result)
    
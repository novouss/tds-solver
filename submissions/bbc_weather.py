
def bbc_weather(city: str) -> str:
    import os
    import re
    import json
    import httpx
    import pandas as pd
    from datetime import datetime
    from urllib.parse import urlencode
    from bs4 import BeautifulSoup
    loc_url = "https://locator-service.api.bbci.co.uk/locations?" + urlencode({
        "api_key": os.environ["BBC_KEY"],
        "s": city,
        "stack": "aws",
        "locale": "en",
        "filter": "international",
        "place-types": "settlement,airport,district",
        "order": "importance",
        "a": "true",
        "format": "json"
    })
    loc_response = httpx.get(loc_url, verify = False)
    result = loc_response.json()
    bbc_url = "https://www.bbc.com/weather/" + result["response"]["results"]["results"][0]["id"]
    response = httpx.get(bbc_url, verify=False)
    # Scrapping BBC
    soup = BeautifulSoup(response.content, "html5lib")
    # Cleaning up
    daily_summary = soup.find("div", attrs={ "class": "wr-day-summary" })
    daily_summary_values = re.findall("[a-zA-Z][^A-Z]*", daily_summary.get_text())
    daily_dates = pd.date_range(datetime.today(), periods=len(daily_summary_values)).to_list()
    daily_dates_values = [daily_dates[i].date().strftime("%Y-%m-%d") for i in range(len(daily_dates))]
    result = { dates: summary for dates, summary in zip(daily_dates_values, daily_summary_values) }
    return str(json.dumps(result))

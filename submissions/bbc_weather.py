
def bbc_weather(city: str) -> str:
    """ Fetches the weather forecast data from BBC Weather API and parses it to get the current and future day's weather summaries.

    Args:
        city (str): The name of the city for which the weather is required.

    Returns:
        str: A JSON string containing the weather summary data.

    Example:
        >>> bbc_weather("London")
        \"\"\"
        {
            "2025-02-11": "Sunny intervals and light winds",
            "2025-02-12": "Light rain showers and a gentle breeze",
            "2025-02-13": "Light rain showers and light winds",
            "2025-02-14": "Light rain showers and a gentle breeze",
            "2025-02-15": "Light rain showers and a gentle breeze",
            "2025-02-16": "Sunny and light winds",
            "2025-02-17": "Sunny intervals and light winds",
            "2025-02-18": "Sunny intervals and light winds",
            "2025-02-19": "Sunny intervals and light winds",
            "2025-02-20": "Light rain and light winds",
            "2025-02-21": "Light cloud and light winds",
            "2025-02-22": "Sunny and light winds",
            "2025-02-23": "Light rain showers and light winds",
            "2025-02-24": "Sunny intervals and light winds"
        }
        \"\"\"
    """
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

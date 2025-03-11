
def counting_days(days: str, datepath: str) -> int:
    """ Counts the number of occurrences of a specific day of the week in a list of dates provided in the datepath.
    
    Args:
        days (str): The day of the week. The string can also end with "day" or "days" (e.g., "Monday", "Mondays", "mon").
        datepath (str): The file path containing the list of dates.
        
    Returns:
        int: The count of how many times the day of the week appeared in the provided list of dates.
    
    Example:
        >>> counting_days("WEDNESDAYS", "dates.txt")
        38
    """
    from dateutil.parser import parse
    
    with open(datepath, "r") as file:
        dates = file.readlines()
    
    day_number = {
        "mon": 0,
        "tue": 1,
        "wed": 2,
        "thurs": 3,
        "fri": 4,
        "sat": 5,
        "sun": 6
    }
    
    days = days.lower()
    
    if days.endswith("days"):
        days = days[:len("days")]
    elif days.endswith("day"):
        days = days[:len("day")]
    
    count_days = 0
    
    for date_str in dates:
        date_str = date_str.strip()
        try:
            date = parse(date_str)
            if date.weekday() == day_number[days]:
                count_days += 1
        except ValueError:
            continue
    return count_days

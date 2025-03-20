
def counting_days(day: str = "Wednesdays", start: str = "1986-11-29", end: str = "2008-08-14") -> str:
    """ Calculates the total number of day of the week between two dates.

    Args:
        day (str): The day of the week to calculate for Mondays, Tues, Wed, THURS, fri, Saturday, or Sunday
        start (str): The start date in 'year-month-day' format
        end (str): The end date in 'year-month-day' format

    Returns:
        str: The total number of of day of the week between the two dates

    Raises:
        ValueError: If the day of the week is not one of 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', or 'sun'

    Example:
        >>> counting_days('wed', '2022-01-01', '2022-12-31')
        '13'
    """
    def day_to_number(day: str) -> int:
        day = day.lower()[:3]
        days = {
            "mon": 0,
            "tue": 1,
            "wed": 2,
            "thu": 3,
            "fri": 4,
            "sat": 5,
            "sun": 6
        }
        return days[day]
    import datetime

    # Assuming start and end dates are formatted like as year-month-day
    start = start.split("-")
    end = end.split("-")

    start_date = datetime.datetime(int(start[0]), int(start[1]), int(start[2]))
    end_date = datetime.datetime(int(end[0]), int(end[1]), int(end[2]))
    days_diff = (end_date - start_date).days
    full_weeks = days_diff // 7
    remaining_days = 1 if days_diff % 7 >= day_to_number(day) else 0
    results = full_weeks + remaining_days
    return str(results)

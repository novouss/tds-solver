
def bounding_box(city: str, country: str) -> str:
    """ Finds the maximum bounding box for a given address.

    Args:
        city (str): The name of the city.
        country (str): The name of the country.

    Returns:
        str: The maximum latitude value from the bounding box coordinates in decimal degrees format.

    Example:
        >>> bounding_box("Hyderabad", "India")
        17.5608321
    """
    from geopy.geocoders import Nominatim
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(", ".join([city, country]))
    raw = location.raw
    max_bounding_box = max(raw["boundingbox"][:2])
    return max_bounding_box

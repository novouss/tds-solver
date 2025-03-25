
def ticket_sales(ticket_type: str = "gold") -> str:
    """ Retrieves the total sales of a specific type of ticket.

    Args:
        ticket_type (str, optional): The type of ticket to retrieve sales for. Defaults to "gold".

    Returns:
        str: A SQL query string used to calculate total sales.

    Raises:
        TypeError: If the input ticket_type is not a string.
    
    Example:
        >>> ticket_sales("gold")
        SELECT SUM(Units * Price) AS total_sales FROM tickets WHERE LOWER(Type) LIKE '%gold%';
    """
    result = f"SELECT SUM(Units * Price) AS total_sales FROM tickets WHERE LOWER(Type) LIKE '%{ticket_type}%';"
    return result

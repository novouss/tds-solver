
def colab_key() -> str:
    """ Hashes a combination of the user's email and expiration year for Google Colab authentication.
    
    Returns:
        str: A 5-character hash value
        
    Raises:
        TypeError: If the input values are not in the correct format.
        
    Example:
        >>> colab_key()
        'af190'
    """
    import hashlib
    email = "raymondbrian.gorospe@straive.com"
    expiry_year = "2025"
    hashed = hashlib.sha256(f"{ email } { expiry_year }".encode()).hexdigest()[-5:] 
    return hashed

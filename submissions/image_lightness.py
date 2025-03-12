
def image_lightness(path: str) -> str:
    """ Calculates the number of pixels with lightness above a certain threshold.

    Args:
        path (str): The path to the image file

    Returns:
        str: A string representation of the count of pixels meeting the threshold condition

    Raises:
        FileNotFoundError: If the specified image file does not exist
        ValueError: If the image is not in RGB mode

    Example:
        >>> image_lightness("./data/image.jpg")
        '198058'
    """
    from PIL import Image
    import numpy as np
    import colorsys
    image = Image.open(path)
    rgb = np.array(image) / 255.0
    lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
    results = np.sum(lightness > 0.402)
    return str(results)

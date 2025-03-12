
def image_lightness(path: str) -> str:
    from PIL import Image
    import numpy as np
    import colorsys

    image = Image.open(path)
    rgb = np.array(image) / 255.0
    lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
    results = np.sum(lightness > 0.402)
    return str(results)
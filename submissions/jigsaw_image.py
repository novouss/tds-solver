
from typing import List, Tuple

ORIGINAL = [
    [(2, 1), (1, 1), (4, 1), (0, 3), (0, 1)],
    [(1, 4), (2, 0), (2, 4), (4, 2), (2, 2)],
    [(0, 0), (3, 2), (4, 3), (3, 0), (3, 4)],
    [(1, 0), (2, 3), (3, 3), (4, 4), (0, 2)],
    [(3, 1), (1, 2), (1, 3), (0, 4), (4, 0)]
]

def jigsaw_image(path: str, original: List[Tuple[int, int]] = ORIGINAL):
    from PIL import Image
    from submissions import encode_image
    
    image = Image.open(path)
    
    z_score = 5
    
    std = (image.size[0]/z_score, image.size[1]/z_score)
    
    crops = []
    x1, y1 = 0, 0
    x2, y2 = std
    for row in range(z_score):
        crop = []
        for col in range(z_score):
            crop.append(image.crop((x1, y1, x2, y2)))
            x1 = x2
            x2 = x2 + std[0]
        crops.append(crop)
        x1 = 0
        y1 = y1 + std[1]
        x2 = std[0]
        y2 = y2 + std[1]

    new_image = Image.new("RGB", (500, 500), "white")
    
    for row, crop in enumerate(crops):
        for col, crop in enumerate(crop):
            pos = original[row][col]
            x = int(pos[1] * std[0])
            y = int(pos[0] * std[1])
            new_image.paste(image, (x, y))
    
    output = "./data/jigsaw.png"
    new_image.save(output)
    
    b64 = encode_image(output)
    
    return b64

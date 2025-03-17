
def encode_image(path: str) -> str:
    """ Encode an image at the given path into a base64 encoded string that can be sent to an AI model for text extraction.

    Args:
        path (str): The file path of the image to be encoded.

    Returns:
        str: A json body of the image to be sent to an AI model.

    Raises:
        FileNotFoundError: If the specified image file does not exist.
        Exception: Any other errors that occur during encoding or sending the request.
    """
    import json
    import base64
    with open(path, "rb") as img:
        image = base64.b64encode(img.read()).decode("utf-8")
    image_url = f"data:image/png;base64,{image}"
    body = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": "What is in this image?" },
                    {
                        "type": "image_url",
                        "image_url": { "url": image_url }
                    }
                ]
            }
        ]
    }
    result = json.dumps(body)
    return str(result)

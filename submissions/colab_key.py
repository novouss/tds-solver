
def colab_key() -> str:
    # import os
    # import httpx
    import hashlib
    # KEY = os.environ["COLAB_TOKEN"]
    # response = httpx.get(
    #     "https://www.googleapis.com/oauth2/v1/userinfo",
    #     params={"alt": "json"},
    #     headers={"Authorization": f"Bearer { KEY }"}
    # )
    email = "raymondbrian.gorospe@straive.com"
    expiry_year = "2025"
    hashed = hashlib.sha256(f"{ email } { expiry_year }".encode()).hexdigest()[-5:] 
    return hashed

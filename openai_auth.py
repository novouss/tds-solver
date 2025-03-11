
import os
from openai import OpenAI

URL = "https://llmfoundry.straive.com/openai/v1/"
KEY = os.environ["AIPROXY_TOKEN"]

client = OpenAI(
    base_url=URL,
    api_key=KEY
)

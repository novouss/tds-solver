
import os
from openai import OpenAI
from typing import List, Dict, Any

URL = "https://llmfoundry.straive.com/openai/v1/"
KEY = os.environ["AIPROXY_TOKEN"]

client = OpenAI(
    base_url = URL,
    api_key = KEY
)

model = "gpt-4o-mini"

def ask_something(prompt: str) -> str:
    response = client.chat.completions.create(
        model = model,
        messages = [
            { "role": "user", "content": prompt }
        ]
    )
    return response.choices[0].message.content

def ask_someone(system: str, prompt: str) -> str:
    response = client.chat.completions.create(
        model = model,
        messages = [
            { "role": "system", "content": system },
            { "role": "user", "content": prompt }
        ]
    )
    return response.choices[0].message.content

def generate_embeddings(text: str) -> List[float]:
    response = client.embeddings.create(
        model = "text-embedding-3-small",
        input = text
    )
    embeddings = response.data[0].embedding
    return embeddings

def ask_tools(prompt: str, tools: list[Dict[str, Any]]):
    response = client.chat.completions.create(
        model = model,
        messages = [
            { "role": "user", "content": prompt }
        ],
        functions = tools,
        function_call = "auto"
    )
    return response.choices[0].message.function_call

"""
openai_client.py
~~~~~~~~~~~~~~~~
Reusable OpenAI client that reads credentials from the environment.

Usage
-----
    from openai_client import get_client, DEFAULT_MODEL

    client = get_client()
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": "Hello!"}],
    )
    print(response.choices[0].message.content)
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Load variables from a local .env file if one exists (ignored in production
# environments where variables are injected directly).
load_dotenv()

DEFAULT_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")


def get_client() -> OpenAI:
    """Return an authenticated :class:`openai.OpenAI` client.

    The API key is read from the ``OPENAI_API_KEY`` environment variable.
    Raises :class:`ValueError` if the variable is not set.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable is not set. "
            "Copy .env.example to .env and add your key, or export the "
            "variable directly in your shell."
        )
    return OpenAI(api_key=api_key)

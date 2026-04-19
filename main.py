"""
main.py
~~~~~~~
Entry point — verifies the OpenAI connection and sends a simple test message.

Run
---
    python main.py
"""

from openai_client import DEFAULT_MODEL, get_client


def main() -> None:
    print("Connecting to OpenAI…")
    client = get_client()

    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": "Say 'OpenAI connection successful!' and nothing else."}],
        max_tokens=20,
    )

    if not response.choices:
        raise RuntimeError("OpenAI returned an empty response — no choices available.")
    message = response.choices[0].message.content
    print(f"Response: {message}")
    print("Connection verified ✓")


if __name__ == "__main__":
    main()

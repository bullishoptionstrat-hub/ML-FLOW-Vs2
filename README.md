# ML-FLOW-Vs2

Machine learning for agents and most LLMs.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure your OpenAI API key

Copy the example environment file and add your key:

```bash
cp .env.example .env
# then edit .env and replace the placeholder with your real key
```

Your `.env` file should look like this:

```
OPENAI_API_KEY=sk-...
```

> **Security note:** `.env` is listed in `.gitignore` and will never be committed.  
> Obtain your API key at <https://platform.openai.com/account/api-keys>.

### 3. Verify the connection

```bash
python main.py
```

Expected output:

```
Connecting to OpenAI…
Response: OpenAI connection successful!
Connection verified ✓
```

## Usage in your own code

```python
from openai_client import get_client, DEFAULT_MODEL

client = get_client()

response = client.chat.completions.create(
    model=DEFAULT_MODEL,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

## Environment variables

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | ✅ Yes | Your OpenAI secret API key |
| `OPENAI_MODEL` | No | Model to use (default: `gpt-4o`) |

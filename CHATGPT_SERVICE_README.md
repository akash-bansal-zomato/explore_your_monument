
# ChatGPT Service Documentation

A simple service for interacting with OpenAI's ChatGPT API.

## Overview

The [`chatgpt_service.py`](chatgpt_service.py:1) module provides a `ChatGPTService` class that wraps the OpenAI API, making it easy to send questions to ChatGPT and receive answers.

## Installation

Install the required dependency:

```bash
pip install openai==1.54.0
```

Or install all project dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Get Your API Key

1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create a new API key
3. Copy the key (it will only be shown once)

### 2. Configure the Service

You have two options:

**Option A: Set API key in code**
```python
from chatgpt_service import chatgpt_service

# Set your API key
chatgpt_service.set_api_key("your-actual-api-key-here")
```

**Option B: Modify the placeholder in [`chatgpt_service.py`](chatgpt_service.py:21)**
```python
# Replace "YOUR_OPENAI_API_KEY_HERE" with your actual key
self.api_key = api_key or "sk-your-actual-key-here"
```

## Usage

### Basic Usage

```python
from chatgpt_service import chatgpt_service

# Ask a question
result = chatgpt_service.get_answer("What is the capital of France?")

# Check if successful
if result["success"]:
    print(f"Answer: {result['answer']}")
    print(f"Tokens used: {result['usage']['total_tokens']}")
else:
    print(f"Error: {result['error']}")
```

### Advanced Usage

```python
from chatgpt_service import ChatGPTService

# Create a new instance with custom API key
service = ChatGPTService(api_key="your-api-key")

# Use a different model
service.set_model("gpt-4")

# Ask a question with specific model
result = service.get_answer(
    "Explain quantum computing",
    model="gpt-4"
)
```

## API Reference

### `ChatGPTService` Class

#### Constructor

```python
ChatGPTService(api_key: Optional[str] = None)
```

**Parameters:**
- `api_key` (str, optional): OpenAI API key. Defaults to "YOUR_OPENAI_API_KEY_HERE"

#### Methods

##### `get_answer(question: str, model: Optional[str] = None) -> dict`

Send a question to ChatGPT and get the answer.

**Parameters:**
- `question` (str): The question to ask ChatGPT
- `model` (str, optional): Model to use. Defaults to "gpt-3.5-turbo"

**Returns:**
```python
{
    "success": True,
    "answer": "The capital of France is Paris.",
    "model": "gpt-3.5-turbo",
    "usage": {
        "prompt_tokens": 15,
        "completion_tokens": 8,
        "total_tokens": 23
    },
    "finish_reason": "stop"
}
```

Or on error:
```python
{
    "success": False,
    "error": "Error message here",
    "answer": None
}
```

##### `set_api_key(api_key: str)`

Update the API key.

**Parameters:**
- `api_key` (str): New OpenAI API key

##### `set_model(model: str)`

Update the default model.

**Parameters:**
- `model` (str): Model name (e.g., "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo")

## Available Models

- **gpt-3.5-turbo** (default): Fast, cost-effective for most tasks
- **gpt-4**: More capable, better for complex reasoning
- **gpt-4-turbo**: Latest GPT-4 model with improved performance

See [OpenAI Models](https://platform.openai.com/docs/models) for full list.

## Testing

Run the test script:

```bash
python test_chatgpt_service.py
```

**Note:** You need to set a valid API key before running the test.

## Example Integration

Here's how to integrate with your existing API:

```python
from flask import Flask, request, jsonify
from chatgpt_service import chatgpt_service

app = Flask(__name__)

# Set your API key
chatgpt_service.set_api_key("your-api-key-here")

@app.route("/ask-chatgpt", methods=['POST'])
def ask_chatgpt():
    data = request.get_json()
    question = data.get("question")
    
    if not question:
        return jsonify({"error": "Question is required"}), 400
    
    # Get answer from ChatGPT
    result = chatgpt_service.get_answer(question)
    
    if result["success"]:
        return jsonify({
            "answer": result["answer"],
            "model": result["model"],
            "tokens_used": result["usage"]["total_tokens"]
        })
    else:
        return jsonify({"error": result["error"]}), 500
```

## Cost Considerations

ChatGPT API calls are billed based on token usage:

- **GPT-3.5-Turbo**: ~$0.002 per 1K tokens
- **GPT-4**: ~$0.03-0.06 per 1K tokens

The service returns token usage in the response, so you can track costs.

## Error Handling

The service handles various errors:

1. **Invalid API Key**: Returns error in response
2. **Network Issues**: Returns error in response
3. **Rate Limits**: Returns error in response
4. **Invalid Model**: Returns error in response

Always check `result["success"]` before using the answer.

## Security Notes

⚠️ **Important Security Practices:**

1. **Never commit API keys to version control**
2. Use environment variables for API keys in production:
   ```python
   import os
   api_key = os.getenv("OPENAI_API_KEY")
   chatgpt_service.set_api_key(api_key)
   ```
3. Add `.env` files to `.gitignore`
4. Rotate API keys regularly
5. Monitor API usage on OpenAI dashboard

## Troubleshooting

### "Unresolved reference 'openai'" error

Install the OpenAI package:
```bash
pip install openai==1.54.0
```

### "Authentication failed" error

Check that your API key is valid and correctly set.

### "Rate limit exceeded" error

You've exceeded your API quota. Check your OpenAI dashboard or wait before retrying.

## License

This service is part of your Audio Generation API project.

## Support

For OpenAI API issues, see:
- [OpenAI Documentation](https://platform.openai.com/docs)
- [OpenAI Community](https://community.openai.com/)

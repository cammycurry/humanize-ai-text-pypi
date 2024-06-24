# Humanize AI Text SDK

This SDK provides easy access to the [Humanize AI Text](https://humanize-ai-text.ai/docs) API, allowing you to humanize AI-generated text effortlessly.

## Installation

You can install the Humanize AI Text SDK using pip:

```bash
pip install humanize-ai-text
```

## Usage

Here's a basic example of how to use the Humanize AI Text SDK:

```python
from humanize_ai_text import HumanizedAI

humanizer = HumanizedAI(api_key='your-api-key-here')

try:
    result = humanizer.run('Your text to humanize goes here.')
    print(result['humanizedText'])
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

## API Reference

### `HumanizedAI(api_key, base_url=None)`

Creates a new instance of the HumanizedAI client.

- `api_key` (required): Your API key for the Humanize AI Text service.
- `base_url` (optional): The base URL for the API. Defaults to 'https://api.humanize-ai-text.ai/v1'.

### `run(text)`

Humanizes the given text.

- `text`: The text to humanize.

Returns a dictionary with the following structure:

```python
{
    'success': bool,
    'input_words': int,
    'output_words': int,
    'humanizedText': str
}
```

## Error Handling

The SDK raises `requests.exceptions.RequestException` for API-related errors. You can catch these exceptions to handle errors in your code.

Example error handling:

```python
from humanize_ai_text import HumanizedAI
import requests

humanizer = HumanizedAI(api_key='your-api-key-here')

try:
    result = humanizer.run('Your text here')
    print(result['humanizedText'])
except requests.exceptions.RequestException as e:
    print(f"API Error: {str(e)}")
    if hasattr(e, 'response'):
        print(f"Status: {e.response.status_code}")
        print(f"Response: {e.response.text}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
```

## Important Information

1. **API Key Security**: Never expose your API key in client-side code. Always use this SDK in a secure server-side environment.

2. **Rate Limiting**: Be aware of any rate limits imposed by the Humanize AI Text API. Implement appropriate error handling for rate limit errors.

3. **Input Text Length**: There may be limitations on the length of text that can be processed in a single request. Refer to the API documentation for specific limits.

4. **Error Handling**: Implement robust error handling in your application to gracefully handle API errors and network issues.

5. **API Versioning**: The SDK defaults to the latest version of the API. If you need to use a specific version, you can set the `base_url` parameter when creating the HumanizedAI instance.

## Support

For additional support or to learn more about our services, please visit our website at [https://humanize-ai-text.ai](https://humanize-ai-text.ai).

## License

MIT
# humanize-ai-text-pypi

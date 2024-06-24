import json
from urllib import request, error


class HumanizedAI:
    def __init__(self, api_key, base_url="https://api.humanize-ai-text.ai/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def run(self, text):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = json.dumps({"text": text}).encode('utf-8')
        req = request.Request(f"{self.base_url}/humanize",
                              data=data, headers=headers, method='POST')

        try:
            with request.urlopen(req) as response:
                return json.loads(response.read().decode('utf-8'))
        except error.HTTPError as e:
            raise HumanizedError(
                f"HTTP error occurred: {e.code} {e.reason}", status=e.code, response=e.read().decode('utf-8'))
        except error.URLError as e:
            raise HumanizedError(f"URL error occurred: {e.reason}")


class HumanizedError(Exception):
    def __init__(self, message, status=None, response=None):
        super().__init__(message)
        self.status = status
        self.response = response

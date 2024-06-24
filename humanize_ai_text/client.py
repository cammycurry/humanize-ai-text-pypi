import requests


class HumanizedAI:
    def __init__(self, api_key, base_url="https://api.humanize-ai-text.ai/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def run(self, text):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(
            f"{self.base_url}/humanize",
            json={"text": text},
            headers=headers
        )
        response.raise_for_status()
        return response.json()


class HumanizedError(Exception):
    def __init__(self, message, status=None, response=None):
        super().__init__(message)
        self.status = status
        self.response = response

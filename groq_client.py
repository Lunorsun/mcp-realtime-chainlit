import os
from typing import Any, Dict, Optional

import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_PROJECT_ID = os.getenv("GROQ_PROJECT_ID")
GROQ_REGION = os.getenv("GROQ_REGION")
GROQ_MODEL = os.getenv("GROQ_MODEL")


class GroqClient:
    """Minimal Groq API client for text generation.

    This is a small helper that posts to Groq's model outputs endpoint.
    Adjust the payload (keys like `input`, `max_output_tokens`, or other
    model-specific parameters) according to the Groq documentation for the
    model you selected.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        project_id: Optional[str] = None,
        region: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self.api_key = api_key or GROQ_API_KEY
        self.project_id = project_id or GROQ_PROJECT_ID
        self.region = region or GROQ_REGION
        self.model = model or GROQ_MODEL

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is required")
        if not self.model:
            raise ValueError("GROQ_MODEL is required")

        # Base URL — if Groq requires region/project in host, adapt here.
        self.base_url = f"https://api.groq.com/v1/models/{self.model}/outputs"

    def generate(
        self, prompt: str, max_output_tokens: int = 512, temperature: float = 0.0
    ) -> Dict[str, Any]:
        """Send a generation request to Groq.

        Returns the parsed JSON response. The exact response format depends on
        the model and Groq API version.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        # Basic payload. If your selected Groq model expects a different schema
        # (for example `input` as an array of messages, or a `parameters` block),
        # change this accordingly.
        payload = {
            "input": prompt,
            "max_output_tokens": max_output_tokens,
            "temperature": temperature,
        }

        if self.project_id:
            # Some Groq setups accept project as query param — include if needed.
            url = f"{self.base_url}?project={self.project_id}"
        else:
            url = self.base_url

        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        return resp.json()


def create_default_client() -> GroqClient:
    return GroqClient()


if __name__ == "__main__":
    # Simple local test (requires env vars set)
    client = create_default_client()
    prompt = "Hello from Groq Llama! Summarize this sentence."
    print(client.generate(prompt))

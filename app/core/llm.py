import requests
import json
from config import Config

class LLM:
    def __init__(self, model=Config.MODEL_NAME):
        self.model = model
        self.base_url = Config.OLLAMA_BASE_URL

    def generate(self, prompt, system_prompt=None, stop=None):
        url = f"{self.base_url}/api/generate"
        
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"System: {system_prompt}\nUser: {prompt}"

        data = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "num_ctx": 4096
            }
        }
        if stop:
            data["stop"] = stop
        
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            return f"Error communicating with Ollama: {e}"

    def chat(self, messages):
        url = f"{self.base_url}/api/chat"
        data = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json().get("message", {}).get("content", "")
        except requests.exceptions.RequestException as e:
             return f"Error communicating with Ollama: {e}"

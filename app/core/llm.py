import requests
import json
from config import Config

class LLM:
    def __init__(self, model=None):
        self.model = model if model else Config.MODEL_NAME
        self.base_url = Config.OLLAMA_BASE_URL

    @staticmethod
    def classify_request(user_input):
        """
        Classify if a request is coding-related or general.
        
        Args:
            user_input: The user's request string
            
        Returns:
            'coding' or 'general'
        """
        user_input_lower = user_input.lower()
        
        # Keywords that indicate coding tasks
        coding_keywords = [
            'code', 'program', 'script', 'function', 'class', 'method',
            'debug', 'error', 'bug', 'implement', 'create file', 'write file',
            'read file', 'list file', 'command', 'execute', 'run',
            'python', 'javascript', 'java', 'c++', 'html', 'css',
            'variable', 'loop', 'array', 'algorithm', 'syntax',
            'compile', 'build', 'deploy', 'test', 'unit test',
            'api', 'database', 'sql', 'json', 'xml'
        ]
        
        # Tool-related patterns
        tool_patterns = [
            'action:', 'action input:', 'read_file', 'write_file',
            'list_files', 'run_command', 'search_web'
        ]
        
        # Check for coding keywords
        for keyword in coding_keywords:
            if keyword in user_input_lower:
                return 'coding'
        
        # Check for tool patterns
        for pattern in tool_patterns:
            if pattern in user_input_lower:
                return 'coding'
        
        # Default to general for conversational queries
        return 'general'
    
    @staticmethod
    def select_model(user_input):
       
        request_type = LLM.classify_request(user_input)
        
        if request_type == 'coding':
            return Config.CODING_MODEL_NAME
        else:
            return Config.GENERAL_MODEL_NAME

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

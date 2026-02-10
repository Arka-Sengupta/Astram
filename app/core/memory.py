import json
import os
from config import Config

class Memory:
    def __init__(self):
        self.memory_file = Config.MEMORY_FILE
        self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {"short_term": [], "long_term": {}}

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_message(self, role, content):
        self.data["short_term"].append({"role": role, "content": content})
        self.save_memory()

    def get_context(self):
        return self.data["short_term"]
    
    def clear_short_term(self):
        self.data["short_term"] = []
        self.save_memory()

    def set_long_term(self, key, value):
        self.data["long_term"][key] = value
        self.save_memory()
    
    def get_long_term(self, key):
        return self.data["long_term"].get(key)

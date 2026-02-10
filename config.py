import os

class Config:
    OLLAMA_BASE_URL = "http://localhost:11434"
    MODEL_NAME = "deepseek-coder:6.7b"
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    MEMORY_FILE = os.path.join(PROJECT_ROOT, "memory.json")

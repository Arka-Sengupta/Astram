import os

class Config:
    OLLAMA_BASE_URL = "http://localhost:11434"
    
    # Model configurations
    CODING_MODEL_NAME = "deepseek-coder:6.7b"  # For coding tasks
    GENERAL_MODEL_NAME = "llama3"  # For general questions
    MODEL_NAME = CODING_MODEL_NAME  # Default model
    
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    MEMORY_FILE = os.path.join(PROJECT_ROOT, "memory.json")

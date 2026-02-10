import requests
import json
import sys
import os

# Add current directory to sys.path to ensure imports work
sys.path.append(os.getcwd())

try:
    from app.core.agent import agent
except Exception as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def check_ollama():
    print("Checking Ollama connection...")
    try:
        res = requests.get("http://localhost:11434/api/tags")
        if res.status_code == 200:
            print("Ollama is UP.")
            models = [m['name'] for m in res.json()['models']]
            print(f"Available models: {models}")
            return True
        else:
            print(f"Ollama returned status: {res.status_code}")
            return False
    except Exception as e:
        print(f"Ollama Connection Error: {e}")
        return False

def check_agent_generation():
    print("\nChecking Agent Generation...")
    try:
        response = agent.llm.generate("Say 'System Operational'")
        print(f"Agent Response: {response}")
    except Exception as e:
        print(f"Agent Generation Error: {e}")

def check_memory():
    print("\nChecking Memory...")
    try:
        agent.memory.add_message("user", "Verification Test")
        context = agent.memory.get_context()
        print(f"Context Length: {len(context)}")
        print(f"Last Message: {context[-1]}")
    except Exception as e:
        print(f"Memory Error: {e}")

if __name__ == "__main__":
    if check_ollama():
        check_agent_generation()
        check_memory()
    else:
        print("Skipping agent tests due to Ollama failure.")

from app.core.agent import agent

def test_agent_ping():
    print("Testing Agent connection to Ollama...")
    try:
        response = agent.llm.generate("Hello")
        print(f"Ollama Response: {response}")
    except Exception as e:
        print(f"Ollama Error: {e}")

def test_memory():
    print("Testing Memory...")
    agent.memory.add_message("user", "test memory")
    context = agent.memory.get_context()
    print(f"Memory Context: {context}")

if __name__ == "__main__":
    test_agent_ping()
    test_memory()

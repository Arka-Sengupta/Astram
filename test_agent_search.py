"""
Test the full agent integration with web search
"""
from app.core.agent import agent

def test_agent_search():
    print("Testing Agent with Web Search")
    print("="*60)
    
    # Test 1: Ask agent to search for something
    query1 = "find me a video tutorial on building AI agents with Ollama"
    print(f"\nUser: {query1}")
    print("-"*60)
    response = agent.process_request(query1)
    print(f"Agent: {response}")
    print("\n" + "="*60)

if __name__ == "__main__":
    test_agent_search()

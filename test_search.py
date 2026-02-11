"""
Test script to verify web search functionality
"""
from app.core.tools import Tools

def test_web_search():
    tools = Tools()
    
    # Test search
    print("Testing web search for: 'Python tutorial videos'")
    print("="*60)
    result = tools.search_web("Python tutorial videos", max_results=3)
    print(result)
    print("\n" + "="*60)
    
    # Test another search
    print("\nTesting web search for: 'Ollama AI agent tutorial'")
    print("="*60)
    result = tools.search_web("Ollama AI agent tutorial", max_results=3)
    print(result)

if __name__ == "__main__":
    test_web_search()

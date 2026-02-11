"""
Test the dual-model system with various request types
"""
from app.core.llm import LLM
from config import Config

def test_model_classification():
    """Test request classification logic"""
    print("="*60)
    print("TESTING REQUEST CLASSIFICATION")
    print("="*60)
    
    test_cases = [
        # Coding requests
        ("Write a Python function to reverse a string", "coding"),
        ("Create a file called test.txt with hello world", "coding"),
        ("Debug this error in my code", "coding"),
        ("Implement a binary search algorithm", "coding"),
        ("List files in the current directory", "coding"),
        ("Run command to check Python version", "coding"),
        
        # General requests
        ("What is the capital of France?", "general"),
        ("Explain quantum physics to me", "general"),
        ("Tell me a joke", "general"),
        ("What is machine learning?", "general"),
        ("Who won the World Cup in 2022?", "general"),
        ("What's the weather like?", "general"),
    ]
    
    print("\nClassification Results:")
    print("-"*60)
    
    for query, expected in test_cases:
        result = LLM.classify_request(query)
        status = "✓" if result == expected else "✗"
        print(f"{status} [{result:7}] {query}")
        
    print("\n" + "="*60)

def test_model_selection():
    """Test model selection logic"""
    print("\nTESTING MODEL SELECTION")
    print("="*60)
    
    test_cases = [
        ("Write a Python function", Config.CODING_MODEL_NAME),
        ("What is AI?", Config.GENERAL_MODEL_NAME),
    ]
    
    print("\nModel Selection Results:")
    print("-"*60)
    
    for query, expected_model in test_cases:
        selected_model = LLM.select_model(query)
        status = "✓" if selected_model == expected_model else "✗"
        print(f"{status} Query: {query}")
        print(f"   Selected: {selected_model}")
        print(f"   Expected: {expected_model}")
        print()
    
    print("="*60)

if __name__ == "__main__":
    test_model_classification()
    test_model_selection()
    
    print("\n" + "="*60)
    print("MODEL CONFIGURATION")
    print("="*60)
    print(f"Coding Model:  {Config.CODING_MODEL_NAME}")
    print(f"General Model: {Config.GENERAL_MODEL_NAME}")
    print(f"Base URL:      {Config.OLLAMA_BASE_URL}")
    print("="*60)

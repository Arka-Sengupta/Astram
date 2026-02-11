"""
Simple integration test for dual-model agent
"""
from app.core.agent import agent

def test_agent_dual_model():
    print("="*60)
    print("TESTING AGENT WITH DUAL-MODEL SYSTEM")
    print("="*60)
    
    # Test 1: Coding question
    print("\n1. CODING QUESTION TEST")
    print("-"*60)
    query1 = "create a file called hello.txt with content 'Hello World'"
    print(f"User: {query1}")
    print()
    response1 = agent.process_request(query1)
    print(f"Response: {response1[:200]}...")
    
    print("\n" + "="*60)
    
    # Test 2: General question
    print("\n2. GENERAL QUESTION TEST")
    print("-"*60)
    query2 = "what is the capital of Japan?"
    print(f"User: {query2}")
    print()
    response2 = agent.process_request(query2)
    print(f"Response: {response2}")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    try:
        test_agent_dual_model()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

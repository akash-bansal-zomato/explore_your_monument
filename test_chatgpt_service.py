
"""
Test script for ChatGPT Service
"""
from services import chatgpt_service


def test_chatgpt_service():
    """Test the ChatGPT service with a sample question"""
    
    print("=" * 60)
    print("ChatGPT Service Test")
    print("=" * 60)
    print()
    
    # Set API key (replace with actual key to test)
    # chatgpt_service.set_api_key("your-actual-api-key-here")
    
    # Test question
    question = "What is the capital of France?"
    
    print(f"Question: {question}")
    print()
    print("Calling ChatGPT...")
    print()
    
    # Get answer from ChatGPT
    result = chatgpt_service.get_answer(question)
    
    if result["success"]:
        print("✓ Success!")
        print()
        print(f"Answer: {result['answer']}")
        print()
        print(f"Model: {result['model']}")
        print(f"Tokens used: {result['usage']['total_tokens']}")
        print(f"Finish reason: {result['finish_reason']}")
    else:
        print("✗ Failed!")
        print()
        print(f"Error: {result['error']}")
    
    print()
    print("=" * 60)
    print()
    print("Note: To use this service with real API calls:")
    print("1. Get your API key from https://platform.openai.com/api-keys")
    print("2. Replace 'YOUR_OPENAI_API_KEY_HERE' with your actual key")
    print("3. Or use: chatgpt_service.set_api_key('your-key-here')")
    print()


if __name__ == "__main__":
    test_chatgpt_service()

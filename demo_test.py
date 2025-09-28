import requests
import json

def demo_without_api_key():
    """Demo the system structure without needing OpenAI API key."""
    
    BASE_URL = "http://localhost:8000"
    
    # Check available agents
    print("📋 Available Agents:")
    response = requests.get(f"{BASE_URL}/agents")
    agents = response.json()
    for agent in agents:
        print(f"\n🤖 {agent['name']}")
        print(f"   Description: {agent['description']}")
    
    # Show what a task request would look like
    print("\n📝 Example Task Request Structure:")
    example_request = {
        "task_type": "full_analysis",
        "topic": "Impact of AI on Software Development",
        "questions": [
            "How is AI changing coding practices?",
            "What are the most popular AI coding tools?",
        ],
        "report_type": "executive_summary",
        "target_audience": "technical"
    }
    print(json.dumps(example_request, indent=2))
    
    print("\n✅ System is ready! To fully test:")
    print("1. Add your OpenAI API key to .env file")
    print("2. Restart the server")
    print("3. Run: python test_system.py")

if __name__ == "__main__":
    demo_without_api_key()

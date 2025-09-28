import requests
import json
import uuid

BASE_URL = "http://localhost:8000"

def demo_system_capabilities():
    print("🚀 Multi-Agent AI System Demo\n")
    
    # Show system info
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        info = response.json()
        print(f"✅ System Status: {info['status']}")
        print(f"📅 Timestamp: {info['timestamp']}")
        print(f"🔢 Version: {info['version']}\n")
    
    # Show what the system can do
    print("🎯 System Capabilities:")
    print("   - Research Agent: Gathers information on any topic")
    print("   - Analysis Agent: Analyzes data and extracts insights")
    print("   - Report Writer: Creates professional reports")
    print("   - Task Coordinator: Orchestrates multi-agent workflows\n")
    
    # Example workflow
    print("📋 Example Workflow:")
    print("   1. User requests analysis on 'AI in Healthcare'")
    print("   2. Research Agent gathers relevant information")
    print("   3. Analysis Agent processes and finds patterns")
    print("   4. Report Writer creates executive summary")
    print("   5. Results delivered via API\n")
    
    # Show API endpoints
    print("🔌 Available API Endpoints:")
    endpoints = [
        ("GET", "/", "System health check"),
        ("GET", "/docs", "Interactive API documentation"),
        ("GET", "/agents", "List all available agents"),
        ("POST", "/tasks/execute", "Execute a multi-agent task"),
        ("GET", "/tasks/{id}", "Get task status"),
        ("GET", "/tasks", "List all tasks")
    ]
    
    for method, path, desc in endpoints:
        print(f"   {method:6} {path:20} - {desc}")
    
    print("\n✨ The system is ready to use!")
    print("📝 To enable AI features, add your OpenAI API key to .env file")
    print("📚 Visit http://localhost:8000/docs for interactive API testing")

if __name__ == "__main__":
    demo_system_capabilities()

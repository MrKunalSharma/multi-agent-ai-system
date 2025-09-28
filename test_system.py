import requests
import json
from datetime import datetime

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test the health check endpoint."""
    print("🔍 Testing Health Check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("-" * 50)

def test_list_agents():
    """Test listing available agents."""
    print("🤖 Testing List Agents...")
    response = requests.get(f"{BASE_URL}/agents")
    print(f"Status Code: {response.status_code}")
    print(f"Available Agents: {json.dumps(response.json(), indent=2)}")
    print("-" * 50)

def test_execute_task():
    """Test executing a full analysis task."""
    print("🚀 Testing Task Execution...")
    
    task_data = {
        "task_type": "full_analysis",
        "topic": "Impact of AI on Software Development in 2024",
        "questions": [
            "How is AI changing coding practices?",
            "What are the most popular AI coding tools?",
            "What are the security implications?"
        ],
        "analysis_type": "comprehensive",
        "report_type": "executive_summary",
        "target_audience": "technical"
    }
    
    print(f"Request Data: {json.dumps(task_data, indent=2)}")
    
    response = requests.post(
        f"{BASE_URL}/tasks/execute",
        json=task_data
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Task ID: {result.get('task_id')}")
        print(f"Status: {result.get('status')}")
        
        # Pretty print the results
        if result.get('results'):
            print("\n📊 Results:")
            
            # Research findings
            if 'research' in result['results']:
                print("\n📚 Research Phase:")
                research = result['results']['research']
                print(f"Status: {research.get('status')}")
                
            # Analysis results  
            if 'analysis' in result['results']:
                print("\n🔍 Analysis Phase:")
                analysis = result['results']['analysis']
                print(f"Status: {analysis.get('status')}")
                
            # Report
            if 'report' in result['results']:
                print("\n📄 Report Phase:")
                report = result['results']['report']
                print(f"Status: {report.get('status')}")
                if report.get('executive_summary'):
                    print(f"\nExecutive Summary:\n{report['executive_summary']}")
                    
        return result.get('task_id')
    else:
        print(f"Error: {response.text}")
        
    print("-" * 50)
    return None

def test_get_task_status(task_id):
    """Test getting task status."""
    if not task_id:
        return
        
    print(f"📋 Testing Get Task Status for ID: {task_id}...")
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print(f"Task Details: {json.dumps(response.json(), indent=2)}")
    print("-" * 50)

def test_list_tasks():
    """Test listing recent tasks."""
    print("📝 Testing List Tasks...")
    response = requests.get(f"{BASE_URL}/tasks?limit=5")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        tasks = response.json()
        print(f"Found {len(tasks)} recent tasks")
        for task in tasks:
            print(f"- Task {task['task_id']}: {task['status']}")
    print("-" * 50)

if __name__ == "__main__":
    print("🧪 Starting Multi-Agent System Tests")
    print("=" * 50)
    
    # Make sure the API is running
    try:
        # Test basic endpoints
        test_health_check()
        test_list_agents()
        
        # Execute a task and get its status
        task_id = test_execute_task()
        
        if task_id:
            import time
            print("\n⏳ Waiting 2 seconds for task to complete...")
            time.sleep(2)
            test_get_task_status(task_id)
            
        test_list_tasks()
        
        print("\n✅ All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to API. Make sure the server is running!")
        print("Run: python -m src.run")

import requests
import json

# Test full task execution
task_data = {
    "task_type": "full_analysis",
    "topic": "Future of Software Development",
    "questions": ["How will AI change coding?"],
    "report_type": "executive_summary",
    "target_audience": "technical"
}

print("🚀 Executing full analysis task...")
response = requests.post("http://localhost:8000/tasks/execute", json=task_data)

if response.status_code == 200:
    result = response.json()
    print(f"✅ Task ID: {result['task_id']}")
    print(f"📊 Status: {result['status']}")
    
    if result.get('results'):
        # Show summary
        if 'summary' in result['results']:
            print(f"\n📝 Summary:")
            print(result['results']['summary'].get('final_output', '')[:500])
        
        # Show report
        if 'report' in result['results']:
            print(f"\n📄 Executive Summary:")
            exec_summary = result['results']['report'].get('executive_summary', '')
            print(exec_summary[:300])

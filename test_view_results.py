import requests
import json

# Get recent tasks
response = requests.get("http://localhost:8000/tasks?limit=10")
if response.status_code == 200:
    tasks = response.json()
    
    # Find the first successful task
    for task in tasks:
        if task['status'] == 'completed':
            print(f"📋 Task ID: {task['task_id']}")
            print(f"✅ Status: {task['status']}")
            print(f"📊 Topic: {task['input_data'].get('topic', 'N/A')}")
            
            if task.get('output_data') and task['output_data'].get('results'):
                results = task['output_data']['results']
                
                # Show report
                if 'report' in results and results['report'].get('report'):
                    report_text = results['report']['report']
                    print("\n📝 Generated Report:")
                    print("-" * 50)
                    print(report_text[:1000])
                    print("-" * 50)
            break
    else:
        print("No successful tasks found")

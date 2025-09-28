# Multi-Agent AI System

A production-ready Multi-Agent AI System where specialized AI agents collaborate to research, analyze, and generate comprehensive reports on any topic.

## 🌟 Features

- **Multi-Agent Architecture**: Specialized agents for research, analysis, and report writing
- **Task Orchestration**: Intelligent coordination between multiple agents
- **Local LLM Support**: Cost-efficient operation using Ollama
- **RESTful API**: Full-featured API with interactive documentation
- **Database Persistence**: Complete task tracking and agent decision logs
- **Async Processing**: High-performance asynchronous task execution

## 🏗️ Architecture



                
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Research Agent │────▶│ Analysis Agent │────▶│ Report Writer │
└─────────────────┘ └─────────────────┘ └─────────────────┘
│ │ │
└───────────────────────┴────────────────────────┘
│
┌────────────▼────────────┐
│ Task Coordinator │
└────────────┬────────────┘
│
┌────────────▼────────────┐
│ FastAPI Backend │
└─────────────────────────┘




## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Ollama installed (for local LLM)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-ai-system.git
cd multi-agent-ai-system


          
Create virtual environment:

          

bash


python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac


                
Install dependencies:

          

bash


pip install -r requirements.txt


                
Set up environment variables:

          

bash


cp .env.example .env
# Edit .env with your configurations


                
Running the System
Start the API server:

          

bash


python test_server.py


                
Access the system:
API: http://localhost:8000
Interactive Docs: http://localhost:8000/docs
Run a test task:

          

bash


python test_full_workflow.py


                
📖 API Usage
Execute a Full Analysis Task

          

python


import requests

task_data = {
    "task_type": "full_analysis",
    "topic": "Impact of AI on Healthcare",
    "questions": [
        "What are the main applications?",
        "What are the challenges?"
    ],
    "report_type": "executive_summary",
    "target_audience": "technical"
}

response = requests.post("http://localhost:8000/tasks/execute", json=task_data)
result = response.json()
print(f"Task ID: {result['task_id']}")


                
Check Task Status

          

python


task_id = "your-task-id"
response = requests.get(f"http://localhost:8000/tasks/{task_id}")
status = response.json()


                
🤖 Available Agents
Research Agent: Gathers comprehensive information on topics
Analysis Agent: Analyzes data and extracts actionable insights
Report Writer: Creates professional reports and summaries
Task Coordinator: Orchestrates multi-agent workflows
🛠️ Technology Stack
Backend: FastAPI, Python 3.9+
AI/LLM: Ollama (Mistral/Phi models), OpenAI API compatible
Database: SQLAlchemy, SQLite/PostgreSQL
Task Queue: Async processing with asyncio
API Docs: Automatic with Swagger UI
📊 Project Structure



multi-agent-ai-system/
├── src/
│   ├── agents/          # AI agents
│   ├── api/             # FastAPI endpoints
│   ├── core/            # Core utilities
│   └── run.py           # Application entry
├── tests/               # Test files
├── docker/              # Docker configuration
├── requirements.txt     # Dependencies
└── README.md           # This file


          
🔧 Configuration
The system supports multiple LLM backends:

Ollama (default, local, free)
OpenAI API (optional, requires API key)
Configure in .env:




# For Ollama (default)
LLM_BACKEND=ollama

# For OpenAI (optional)
OPENAI_API_KEY=your_key_here
LLM_BACKEND=openai


          
🚢 Deployment
Docker

          

bash


docker-compose up


                
Cloud Deployment
Supports deployment on Railway, Render, AWS, GCP
Environment variables for configuration
Health checks included
📈 Performance
Async processing for high throughput
Local LLM option for zero API costs
Typical task completion: 15-30 seconds
Supports concurrent task execution
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Built with FastAPI
LLM support via Ollama
Inspired by AutoGPT and LangChain architectures
Built by Kunal Sharma | https://www.linkedin.com/in/kunal-sharma-1a8457257/ | https://github.com/MrKunalSharma
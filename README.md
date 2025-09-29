<div align="center">

# Multi-Agent AI System

Collaborative AI agents that research, analyze, and produce concise, professional reports.

[![Deploy - Streamlit](https://img.shields.io/badge/Live_Demo-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://multi-agent-ai-system-asnsejr3pz3v3ntvkdknyd.streamlit.app/) [![API - FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](http://localhost:8000/docs) [![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)

</div>

## Overview

Production-ready multi-agent system where specialized AI agents collaborate to deliver research-driven insights. Includes a FastAPI backend, Streamlit UI, async orchestration, and optional local LLMs via Ollama.

## Table of Contents

- [Live Demo & Links](#live-demo--links)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [API Usage Example](#api-usage-example)
- [Agents](#agents)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Performance](#performance)
- [Development](#development)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## Live Demo & Links

- 🚀 Live Demo: [Streamlit deployment](https://multi-agent-ai-system-asnsejr3pz3v3ntvkdknyd.streamlit.app/)
- 💻 Source: [GitHub Repository](https://github.com/MrKunalSharma/multi-agent-ai-system)
- 📚 API Docs (local): `http://localhost:8000/docs`

## Features

- Multi-agent architecture: research, analysis, and report writing
- Task orchestration and workflow coordination
- Optional local LLMs via Ollama (zero API cost)
- RESTful API with automatic OpenAPI/Swagger docs
- Database persistence for tasks and agent decisions
- High-performance async processing
- Streamlit UI for easy demos

## Architecture

```
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  Research Agent │──▶│  Analysis Agent │──▶│  Report Writer  │
└─────────────────┘   └─────────────────┘   └─────────────────┘
          │                    │                      │
          └──────────────┬─────┴──────────────┬──────┘
                         ▼                    ▼
                  Task Coordinator      FastAPI Backend
```

## Quick Start

### Prerequisites

- Python 3.9+
- Git
- [Ollama](https://ollama.ai/) (optional, for local LLMs)

### Installation

1) Clone and enter the project

```bash
git clone https://github.com/MrKunalSharma/multi-agent-ai-system.git
cd multi-agent-ai-system
```

2) Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3) Install dependencies

```bash
# Full API system
pip install -r requirements-full.txt

# Streamlit demo only
pip install -r requirements.txt
```

4) Optional: Install Ollama models

```bash
# Install Ollama from https://ollama.ai/
ollama pull mistral
ollama pull phi
```

5) Configure environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### Run

Start the API server

```bash
python test_server.py
```

Access the system

- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Streamlit UI: `streamlit run streamlit_app.py`

Run an end-to-end test

```bash
python test_full_workflow.py
```

## API Usage Example

```python
import requests

# Execute a full analysis task
task_data = {
    "task_type": "full_analysis",
    "topic": "Impact of AI on Healthcare",
    "questions": [
        "What are the main applications?",
        "What are the challenges?",
        "What is the future outlook?"
    ],
    "report_type": "executive_summary",
    "target_audience": "technical"
}

response = requests.post("http://localhost:8000/tasks/execute", json=task_data)
result = response.json()

print(f"Task ID: {result['task_id']}")
print(f"Status: {result['status']}")
```

## Agents

| Agent            | Description                      | Capabilities |
|------------------|----------------------------------|--------------|
| Research Agent   | Information gathering specialist | Topic research; data collection; fact finding |
| Analysis Agent   | Data analysis expert             | Pattern recognition; insight extraction; trend analysis |
| Report Writer    | Documentation specialist         | Report generation; executive summaries; professional formatting |
| Task Coordinator | Workflow orchestrator            | Agent coordination; task management; result compilation |

## Technology Stack

| Area             | Choice |
|------------------|--------|
| Backend          | FastAPI (Python 3.9+) |
| AI/LLM           | Ollama (Mistral/Phi), OpenAI-compatible APIs |
| Database         | SQLAlchemy with SQLite/PostgreSQL |
| Task Processing  | asyncio for concurrent execution |
| API Docs         | OpenAPI/Swagger (auto) |
| UI               | Streamlit |
| Deployment       | Docker-ready; Streamlit Cloud |

## Project Structure

```
multi-agent-ai-system/
├── src/
│   ├── agents/          # AI agent implementations
│   ├── api/             # FastAPI endpoints
│   ├── core/            # Core utilities and config
│   └── run.py           # Application entry point
├── tests/               # Test files
├── app.py               # Streamlit demo app
├── streamlit_app.py     # Full Streamlit interface
├── requirements.txt     # Streamlit dependencies
├── requirements-full.txt# Full system dependencies
├── .env.example         # Environment template
├── docker-compose.yml   # Docker configuration
└── README.md            # This file
```

## Configuration

### LLM configuration

```env
# For Ollama (default, local, free)
LLM_BACKEND=ollama
OLLAMA_MODEL=mistral:latest

# For OpenAI (optional, requires API key)
OPENAI_API_KEY=your_key_here
LLM_BACKEND=openai
```

### Database configuration

```env
# SQLite (default)
DATABASE_URL=sqlite:///./multiagent.db

# PostgreSQL (production)
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Deployment

### Local development

```bash
python test_server.py
```

### Docker

```bash
docker-compose up
```

### Cloud options

- Streamlit Cloud: pre-deployed demo
- Railway / Render: use provided Dockerfile
- AWS / GCP / Azure: container-ready architecture

## Performance

- Task completion: ~15–30s average
- Concurrent tasks: multiple simultaneous executions
- Status checks: <100ms
- Zero API costs when using local Ollama

## Development

### Tests

```bash
pytest tests/
```

### Code quality

```bash
# Formatting
black src/

# Linting
flake8 src/
```

## Examples

Example scripts:

- `test_full_workflow.py` – complete task execution
- `test_ollama_integration.py` – Ollama integration test
- `demo_test.py` – API functionality demo

## Contributing

Contributions are welcome! Please open a discussion or submit a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m "Add some AmazingFeature"`
4. Push to your branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## License

MIT License. See `LICENSE`.

## Acknowledgments

- Built with FastAPI
- LLM support via Ollama
- UI powered by Streamlit
- Inspired by AutoGPT and LangChain architectures

## Author

Kunal Sharma

- GitHub: `https://github.com/MrKunalSharma/multi-agent-ai-system`
- Live Demo: `https://multi-agent-ai-system-asnsejr3pz3v3ntvkdknyd.streamlit.app/`

⭐ If you find this project helpful, consider starring the repository!



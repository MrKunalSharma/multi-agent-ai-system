import asyncio
from src.agents.research_agent import ResearchAgent

async def test_research():
    print("🧪 Testing Research Agent with Ollama...")
    
    agent = ResearchAgent()
    result = await agent.execute({
        "topic": "Impact of AI on healthcare",
        "questions": ["What are the main benefits?", "What are the challenges?"]
    })
    
    print(f"\n✅ Status: {result['status']}")
    findings = result.get('research_findings', 'No findings')
    if isinstance(findings, str):
        print(f"📊 Findings: {findings[:200]}...")
    else:
        print(f"📊 Findings: {str(findings)[:200]}...")

if __name__ == "__main__":
    asyncio.run(test_research())

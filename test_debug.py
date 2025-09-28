import asyncio
from src.agents.analysis_agent import AnalysisAgent

async def test_analysis():
    agent = AnalysisAgent()
    result = await agent.execute({
        "research_findings": {"test": "data"},
        "analysis_type": "quick"
    })
    print(f"Result: {result}")

asyncio.run(test_analysis())

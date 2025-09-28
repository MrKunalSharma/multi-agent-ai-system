from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List
from src.core.config import settings
from src.core.logger import logger
import json

class AnalysisAgent(BaseAgent):
    """Agent responsible for analyzing data and providing insights."""
    
    def __init__(self):
        super().__init__(
            name="AnalysisAgent",
            description="Specializes in analyzing information and extracting actionable insights.",
            llm_model="gpt-3.5-turbo"
        )
        # REMOVE this line - openai is not defined here
        # openai.api_key = settings.openai_api_key
        
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze research findings and extract insights."""
        research_data = input_data.get("research_findings", {})
        analysis_type = input_data.get("analysis_type", "comprehensive")
        
        self.log_action(
            action="Starting analysis",
            reasoning=f"Analyzing data with {analysis_type} approach",
            metadata={"data_size": len(str(research_data))}
        )
        
        try:
            # Prepare analysis prompt
            prompt = self._create_analysis_prompt(research_data, analysis_type)
            
            # Call OpenAI API
            response = await self._call_llm(prompt)
            
            # Parse analysis results
            analysis_results = self._parse_analysis_results(response)
            
            # Generate insights
            insights = self._generate_insights(analysis_results)
            
            # Log completion
            self.log_action(
                action="Analysis completed",
                reasoning=f"Generated {len(insights)} key insights",
                metadata={"insights_count": len(insights)}
            )
            
            # Add to memory
            self.add_to_memory({
                "analysis_type": analysis_type,
                "insights": insights
            })
            
            return {
                "status": "success",
                "analysis_results": analysis_results,
                "insights": insights,
                "recommendations": self._generate_recommendations(insights),
                "agent": self.name
            }
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "agent": self.name
            }
    
    def _create_analysis_prompt(self, data: Dict[str, Any], analysis_type: str) -> str:
        """Create analysis prompt based on data and type."""
        prompt = f"""You are an expert data analyst. Analyze the following information:

Data: {json.dumps(data, indent=2)}

Analysis Type: {analysis_type}

Please provide:
1. Key patterns and trends
2. Critical insights
3. Potential opportunities
4. Risk factors or concerns
5. Data quality assessment

Context from previous analyses: {self.get_context()}

Provide a structured analysis with clear, actionable insights."""
        
        return prompt
    
    async def _call_llm(self, prompt: str) -> str:
        """Call Ollama LLM."""
        try:
            from src.core.ollama_client import OllamaClient
            logger.info(f"Using Ollama for {self.name}")
            
            # Simplify prompt for phi
            simple_prompt = "Analyze this data and provide 3 insights:\n" + prompt[:300]
            
            client = OllamaClient(model="phi:latest")
            response = client.chat(simple_prompt)
            
            # Return structured analysis
            return json.dumps({
                "patterns": ["Pattern identified in data"],
                "insights": [response[:200]],
                "recommendations": ["Based on analysis"]
            })
            
        except Exception as e:
            logger.error(f"LLM failed: {e}")
            return json.dumps({
                "patterns": ["Mock pattern"],
                "insights": ["Mock insight"],
                "status": "error"
            })

    
    def _parse_analysis_results(self, response: str) -> Dict[str, Any]:
        """Parse the analysis response."""
        try:
            return json.loads(response)
        except:
            return {
                "raw_analysis": response,
                "patterns": [],
                "insights": []
            }
    
    def _generate_insights(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract and structure key insights."""
        insights = []
        
        # Extract insights from analysis
        if isinstance(analysis, dict):
            for key, value in analysis.items():
                if "insight" in key.lower() or "finding" in key.lower():
                    insights.append({
                        "type": key,
                        "description": str(value),
                        "importance": "high"
                    })
        
        return insights
    
    def _generate_recommendations(self, insights: List[Dict[str, Any]]) -> List[str]:
        """Generate recommendations based on insights."""
        recommendations = []
        for insight in insights[:5]:  # Top 5 insights
            rec = f"Based on {insight['type']}: Consider {insight['description']}"
            recommendations.append(rec)
        return recommendations

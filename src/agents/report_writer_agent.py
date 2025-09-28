from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List
from src.core.config import settings
from src.core.logger import logger
from datetime import datetime
import json

class ReportWriterAgent(BaseAgent):
    """Agent responsible for creating comprehensive reports."""
    
    def __init__(self):
        super().__init__(
            name="ReportWriterAgent",
            description="Specializes in creating well-structured, professional reports.",
            llm_model="gpt-3.5-turbo"
        )
        
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a comprehensive report from research and analysis."""
        research_data = input_data.get("research_findings", {})
        analysis_data = input_data.get("analysis_results", {})
        report_type = input_data.get("report_type", "executive_summary")
        target_audience = input_data.get("target_audience", "general")
        
        self.log_action(
            action="Creating report",
            reasoning=f"Generating {report_type} for {target_audience} audience",
            metadata={"report_type": report_type}
        )
        
        try:
            # Prepare report generation prompt
            prompt = self._create_report_prompt(
                research_data, analysis_data, report_type, target_audience
            )
            
            # Generate report
            report_content = await self._call_llm(prompt)
            
            # Format report
            formatted_report = self._format_report(
                report_content, report_type, target_audience
            )
            
            # Generate executive summary
            executive_summary = await self._generate_executive_summary(formatted_report)
            
            # Log completion
            self.log_action(
                action="Report completed",
                reasoning=f"Successfully generated {report_type} report",
                metadata={"word_count": len(formatted_report.split())}
            )
            
            # Add to memory
            self.add_to_memory({
                "report_type": report_type,
                "summary": executive_summary
            })
            
            return {
                "status": "success",
                "report": formatted_report,
                "executive_summary": executive_summary,
                "metadata": {
                    "created_at": datetime.utcnow().isoformat(),
                    "report_type": report_type,
                    "target_audience": target_audience,
                    "word_count": len(formatted_report.split())
                },
                "agent": self.name
            }
            
        except Exception as e:
            logger.error(f"Report generation failed: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "agent": self.name
            }
    
    def _create_report_prompt(self, research: Dict, analysis: Dict, 
                            report_type: str, audience: str) -> str:
        """Create prompt for report generation."""
        prompt = f"""You are a professional report writer. Create a {report_type} report.

Research Findings:
{json.dumps(research, indent=2)}

Analysis Results:
{json.dumps(analysis, indent=2)}

Target Audience: {audience}
Report Type: {report_type}

Previous reports context: {self.get_context()}

Please create a well-structured report that includes:
1. Executive Summary
2. Key Findings
3. Detailed Analysis
4. Recommendations
5. Conclusion

The report should be:
- Clear and concise
- Professional in tone
- Appropriate for the {audience} audience
- Well-organized with proper headings
- Include data-driven insights"""
        
        return prompt
    
    async def _call_llm(self, prompt: str) -> str:
        """Call Ollama LLM."""
        try:
            from src.core.ollama_client import OllamaClient
            logger.info(f"Using Ollama for {self.name}")
            
            # Simple prompt
            simple_prompt = "Write a brief report:\n" + prompt[:300]
            
            client = OllamaClient(model="phi:latest")
            response = client.chat(simple_prompt)
            
            return response
            
        except Exception as e:
            logger.error(f"LLM failed: {e}")
            return "Report generation failed."
        
        
    async def _generate_executive_summary(self, report: str) -> str:
        """Generate executive summary."""
        try:
            from src.core.ollama_client import OllamaClient
            client = OllamaClient(model="phi:latest")
            
            prompt = f"Summarize in 50 words: {report[:500]}"
            return client.chat(prompt)
            
        except Exception as e:
            logger.error(f"Summary generation failed: {e}")
            return "Executive summary: Report completed successfully."

        
    def _format_report(self, content: str, report_type: str, audience: str) -> str:
        """Format the report with proper structure."""
        formatted = f"""# {report_type.replace('_', ' ').title()} Report

**Generated on:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
**Target Audience:** {audience.title()}

---

{content}

---

*This report was generated by the Multi-Agent AI System*
"""
        return formatted
    
    async def _generate_executive_summary(self, report: str) -> str:
        """Generate a concise executive summary."""
        prompt = f"""Create a concise executive summary (max 200 words) for this report:

{report[:1500]}

Focus on the most critical findings and recommendations."""
        
        try:
            from openai import OpenAI
            client = OpenAI(api_key=settings.openai_api_key)
            
            response = client.chat.completions.create(
                model=self.llm_model,
                messages=[
                    {"role": "system", "content": "You are an expert at creating executive summaries."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Executive summary generation failed: {e}")
            return "Executive summary generation failed."

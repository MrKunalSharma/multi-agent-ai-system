from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
from src.core.logger import logger
from src.core.database import AgentLog, get_db
from sqlalchemy.orm import Session
import json
import uuid

class BaseAgent(ABC):
    """Base class for all AI agents in the system."""
    
    def __init__(self, name: str, description: str, llm_model: str = "gpt-3.5-turbo"):
        self.name = name
        self.description = description
        self.llm_model = llm_model
        self.memory: List[Dict[str, Any]] = []
        self.task_id: Optional[str] = None
        
    def set_task_id(self, task_id: str):
        """Set the current task ID for logging purposes."""
        self.task_id = task_id
        
    def log_action(self, action: str, reasoning: str, metadata: Dict[str, Any] = None):
        """Log agent actions to database."""
        try:
            db = next(get_db())
            log_entry = AgentLog(
                task_id=self.task_id,
                agent_name=self.name,
                action=action,
                reasoning=reasoning,
                meta_data=metadata or {}

            )
            db.add(log_entry)
            db.commit()
            logger.info(f"[{self.name}] Action: {action} | Reasoning: {reasoning}")
        except Exception as e:
            logger.error(f"Failed to log agent action: {e}")
        finally:
            db.close()
    
    def add_to_memory(self, content: Dict[str, Any]):
        """Add information to agent's memory."""
        self.memory.append({
            "timestamp": datetime.utcnow().isoformat(),
            "content": content
        })
        # Keep only last 10 memories to avoid token limits
        if len(self.memory) > 10:
            self.memory = self.memory[-10:]
    
    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the agent's main task."""
        pass
    
    def get_context(self) -> str:
        """Get agent's current context from memory."""
        if not self.memory:
            return "No previous context."
        
        context = "Previous context:\n"
        for mem in self.memory[-3:]:  # Last 3 memories
            context += f"- {json.dumps(mem['content'], indent=2)}\n"
        return context

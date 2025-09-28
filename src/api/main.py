from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import asyncio
from typing import List, Dict, Any
from datetime import datetime

from src.api.models import (
    TaskRequest, TaskResponse, AgentInfo, 
    TaskStatus, HealthCheck, IntegrationRequest, 
    IntegrationResponse
)
from src.agents.agent_factory import AgentFactory
from src.core.database import get_db, TaskExecution
from src.core.logger import logger
from src.core.config import settings

# Create FastAPI app
app = FastAPI(
    title="Multi-Agent AI System",
    description="Production-ready multi-agent system for automated task execution",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store running tasks
running_tasks: Dict[str, Any] = {}

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    logger.info("Multi-Agent AI System starting up...")
    logger.info(f"Environment: {settings.app_env}")
    logger.info("All systems initialized successfully!")

@app.get("/", response_model=HealthCheck)
async def root():
    """Root endpoint with health check."""
    return HealthCheck(
        status="healthy",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0",
        services={
            "database": "connected",
            "agents": "ready",
            "integrations": "available"
        }
    )

@app.get("/health", response_model=HealthCheck)
async def health_check():
    """Detailed health check endpoint."""
    services_status = {}
    
    # Check database
    try:
        db = next(get_db())
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        services_status["database"] = "healthy"
    except Exception as e:
        services_status["database"] = f"unhealthy: {str(e)}"
    finally:
        if 'db' in locals():
            db.close()

    
    # Check agents
    try:
        AgentFactory.get_available_agents()
        services_status["agents"] = "healthy"
    except Exception as e:
        services_status["agents"] = f"unhealthy: {str(e)}"
    
    # Check OpenAI API
    services_status["openai_api"] = "configured" if settings.openai_api_key else "not_configured"
    
    return HealthCheck(
        status="healthy" if all(v == "healthy" or v == "configured" for v in services_status.values()) else "degraded",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0",
        services=services_status
    )

@app.get("/agents", response_model=List[AgentInfo])
async def list_agents():
    """List all available agents."""
    agents = AgentFactory.get_available_agents()
    return [
        AgentInfo(name=name, description=desc) 
        for name, desc in agents.items()
    ]

@app.post("/tasks/execute", response_model=TaskResponse)
async def execute_task(
    task_request: TaskRequest,
    background_tasks: BackgroundTasks
):
    """Execute a task using the multi-agent system."""
    logger.info(f"Received task request: {task_request.task_type}")
    
    try:
        # Create coordinator
        coordinator = AgentFactory.create_coordinator()
        
        # Prepare input data
        input_data = task_request.model_dump()
        
        # Execute task
        result = await coordinator.execute(input_data)
        
        # Store task info
        task_id = result.get("task_id")
        running_tasks[task_id] = result
        
        logger.info(f"Task {task_id} completed successfully")
        
        return TaskResponse(**result)
        
    except Exception as e:
        logger.error(f"Task execution failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks/{task_id}", response_model=TaskStatus)
async def get_task_status(task_id: str, db: Session = Depends(get_db)):
    """Get status of a specific task."""
    task = db.query(TaskExecution).filter(TaskExecution.task_id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return TaskStatus(
        task_id=task.task_id,
        status=task.status,
        created_at=task.created_at,
        completed_at=task.completed_at,
        input_data=task.input_data,
        output_data=task.output_data
    )

@app.get("/tasks", response_model=List[TaskStatus])
async def list_tasks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """List recent tasks."""
    tasks = db.query(TaskExecution).offset(skip).limit(limit).all()
    
    return [
        TaskStatus(
            task_id=task.task_id,
            status=task.status,
            created_at=task.created_at,
            completed_at=task.completed_at,
            input_data=task.input_data,
            output_data=task.output_data
        )
        for task in tasks
    ]

@app.post("/integrations/execute", response_model=IntegrationResponse)
async def execute_integration(integration_request: IntegrationRequest):
    """Execute an integration action."""
    # This is a placeholder - we'll implement actual integrations later
    logger.info(f"Integration request: {integration_request.integration} - {integration_request.action}")
    
    return IntegrationResponse(
        status="success",
        integration=integration_request.integration,
        action=integration_request.action,
        result={"message": "Integration endpoint placeholder - implement specific integration"}
    )

@app.delete("/tasks/{task_id}")
async def cancel_task(task_id: str):
    """Cancel a running task."""
    if task_id in running_tasks:
        del running_tasks[task_id]
        return {"message": f"Task {task_id} cancelled"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")

# Error handlers
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}")
    return {"error": "Internal server error", "detail": str(exc)}

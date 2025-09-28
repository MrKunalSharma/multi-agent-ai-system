from fastapi import FastAPI
import uvicorn

# Try to import our app
try:
    from src.api.main import app
    print("Using main app")
except Exception as e:
    print(f"Could not import main app: {e}")
    print("Using test app")
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"message": "Test server is working!"}

if __name__ == "__main__":
    print("Starting server on http://localhost:8000")
    print("API Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000) 

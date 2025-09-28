import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        # API Keys
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
        self.huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY", "")
        
        # Database
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
        
        # Redis
        self.redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        
        # Integration Keys
        self.notion_api_key = os.getenv("NOTION_API_KEY", "")
        self.slack_bot_token = os.getenv("SLACK_BOT_TOKEN", "")
        self.gmail_credentials_path = os.getenv("GMAIL_CREDENTIALS_PATH", "")
        self.jira_url = os.getenv("JIRA_URL", "")
        self.jira_username = os.getenv("JIRA_USERNAME", "")
        self.jira_api_token = os.getenv("JIRA_API_TOKEN", "")
        
        # App Settings
        self.app_env = os.getenv("APP_ENV", "development")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()

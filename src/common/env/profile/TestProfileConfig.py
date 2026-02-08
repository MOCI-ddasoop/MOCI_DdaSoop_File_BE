from .BaseProfileConfig import BaseProfileConfig

class TestProfileConfig(BaseProfileConfig):
    DATABASE_URL: str = "sqlite:///./test.db"
    SERVER_URL: str = "http://localhost:8000"
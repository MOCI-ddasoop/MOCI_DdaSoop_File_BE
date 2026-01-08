from .BaseProfileConfig import BaseProfileConfig

class DevProfileConfig(BaseProfileConfig):
    DATABASE_URL: str = 'sqlite:///./dev.db'
    SERVER_URL: str = 'http://localhost:8000'


from .BaseProfileConfig import BaseProfileConfig

class ProdProfileConfig(BaseProfileConfig):
    DATABASE_URL: str = 'sqlite:///./database.db'
    SERVER_URL: str = 'http://localhost:8000'
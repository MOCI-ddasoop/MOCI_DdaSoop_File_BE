from pydantic_settings import BaseSettings

class BaseProfileConfig(BaseSettings):
    DATABASE_URL: str
    SERVER_URL: str
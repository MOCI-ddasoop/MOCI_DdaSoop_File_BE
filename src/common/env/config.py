from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROFILE: str
    SERVER_URL: str
    DATABASE_URL: str
    FILE_ROOT_PATH: str
    FILE_BUFFER_SIZE: int

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from common.env.profile import PROFILE_CLASS_MAP, BaseProfileConfig

class Settings(BaseSettings):
    PROFILE: Literal["dev", "prod", "test"] = Field(default="dev")
    FILE_ROOT_PATH: str
    FILE_BUFFER_SIZE: int
    profile_config: BaseProfileConfig | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        frozen=True
    )

    def model_post_init(self, __context) -> None:
        cls = PROFILE_CLASS_MAP[self.PROFILE]
        object.__setattr__(self, "profile_config", cls())

settings = Settings()
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    TG_BOT_TOKEN: str = Field()
    GREETING_TEXT: str = Field(
        alias='GREETING_TEXT',
        default='Welcome to the Telegram bot!',
    )
    DATABASE_NAME: str = Field(default='bot.db')


@lru_cache(1)
def get_settings() -> ProjectSettings:
    return ProjectSettings()

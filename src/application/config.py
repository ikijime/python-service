from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(str, Enum):
    production = "production"
    development = "development"
    testing = "testing"


class Settings(BaseSettings):
    app_env: AppEnv
    db_server_url: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()
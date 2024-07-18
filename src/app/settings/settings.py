import os
from typing import List

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=find_dotenv(), env_file_encoding="utf-8", extra="ignore"
    )

    ALLOWED_HOSTS: List[str] = ["*"]
    VERSION: str

    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_PORT: int
    DB_ENGINE: str

    @property
    def db_url(self) -> str:
        return f"{self.DB_ENGINE}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"


settings = Settings()

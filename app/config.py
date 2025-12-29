from __future__ import annotations
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
  APP_NAME: str = os.getenv("APP_NAME", "fastapi-skeleton")
  APP_VERSION: str = os.getenv("APP_VERSION", "0.0.0")
  DEBUG: bool = os.getenv("DEBUG", "false").lower() in ("1", "true", "yes")
  HOST: str = os.getenv("HOST", "127.0.0.1")
  PORT: int = int(os.getenv("PORT", 8000))
  LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()

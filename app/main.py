from __future__ import annotations
import logging
# from datetime import datetime
from datetime import datetime, UTC

from fastapi import FastAPI
from fastapi.responses import JSONResponse

try:
  from .config import settings
except Exception:
  class _S:
    APP_NAME = "fastapi-skeleton"
    APP_VERSION = "0.0.0"
    LOG_LEVEL = "INFO"
  settings = _S()

try:
  from .models import HealthResponse
except Exception:
  from pydantic import BaseModel

  class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: datetime
    message: str | None = None

# Basic logging
logging.basicConfig(
  level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("Starting application %s version %s", settings.APP_NAME, settings.APP_VERSION)

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

@app.get("/health", response_model=HealthResponse)
def health():
  logger.debug("Health check requested")
  payload = HealthResponse(
    status="ok",
    version=getattr(settings, "APP_VERSION", "0.0.0"),
    timestamp = datetime.now(UTC),
    # timestamp=datetime.utcnow(),
    message="service available",
  )
  # return JSONResponse(status_code=200, content=payload.dict())
  return payload;


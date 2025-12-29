from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime

class HealthResponse(BaseModel):
  status: str
  version: str
  timestamp: datetime
  message: str | None = None

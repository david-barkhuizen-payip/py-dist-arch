from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    timestamp: str
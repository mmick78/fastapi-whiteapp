from pydantic import BaseModel


class HealthCheckDto(BaseModel):
    message: str

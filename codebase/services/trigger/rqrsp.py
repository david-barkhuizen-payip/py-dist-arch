from pydantic import BaseModel, validator

class TriggerRequest(BaseModel):
    pass

class TriggerResponse(BaseModel):
    rsp: str
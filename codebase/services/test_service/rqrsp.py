from pydantic import BaseModel, validator

class TestRequest(BaseModel):
    pass

class TestExport(BaseModel):
    pass
class TestResponse(BaseModel):
    test: TestExport
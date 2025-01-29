from pydantic import BaseModel

class ContentGeneratorData(BaseModel):
    topic: str
    type_of_content: str
    target_audience: str
    language: str

from pydantic import BaseModel

class LifestyleWellnessData(BaseModel):
    goals: str
    activity_level: str
    preferred_styles: str
    health_conditions: str
    language: str

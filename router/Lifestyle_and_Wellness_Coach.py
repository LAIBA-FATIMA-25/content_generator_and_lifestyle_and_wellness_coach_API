from fastapi import APIRouter
from utils.prompts import get_lifestyle_prompt  # Assuming a new prompt function for lifestyle
from services.gemini_service import call_llm
from scehmas.Lifestyle_and_wellness_coach_schemas  import LifestyleWellnessData  # Define a new schema for lifestyle and wellness data

router = APIRouter()

@router.post("/lifestyle_wellness")
def generate_lifestyle_wellness(userInput: LifestyleWellnessData):
    """This route provides lifestyle and wellness tips based on the user's input"""
    
    prompt: str = get_lifestyle_prompt(userInput.goals,
                                       userInput.activity_level,
                                       userInput.preferred_styles,
                                       userInput.health_conditions,
                                       userInput.language)
    response = call_llm(prompt)
    return response

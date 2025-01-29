from fastapi import APIRouter
from utils.prompts import get_lifestyle_prompt, get_content_generator_prompt  # Different prompt functions for each purpose
from services.gemini_service import call_llm

from scehmas.Content_Generator_schemas import ContentGeneratorData  # Define a new schema for content generation

router = APIRouter()

# Content Generator Endpoint
@router.post("/content_generator")
def generate_content(userInput: ContentGeneratorData):
    """This route generates content based on the user's input"""
    
    prompt: str = get_content_generator_prompt(userInput.topic,
                                               userInput.type_of_content,
                                               userInput.target_audience,
                                               userInput.language)
    response = call_llm(prompt)
    return response

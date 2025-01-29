
from langchain_google_genai import GoogleGenerativeAI
from core.key import key_laiba

def call_llm(prompt: str) -> str:
    """This function calls the Google Generative AI model to generate a response based on the prompt."""
    key = key_laiba  # You don't need to assign it twice

    llm = GoogleGenerativeAI(model="gemini-1.5-flash", key=key)
    result = llm.invoke(prompt)
    return result

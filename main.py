from fastapi import FastAPI
import uvicorn as uv
from router.Lifestyle_and_Wellness_Coach import router as lifestyle_wellness_router
from router.Content_Generator import router as content_generator_router


app = FastAPI()

# Include routers
app.include_router(lifestyle_wellness_router, tags=["Lifestyle & Wellness Coach"])
app.include_router(content_generator_router, tags=["Content Generator"])


@app.get("/")
def home():
    return {"message": "Welcome to the AI-powered APIs for Wellness and Content Generation!"}

def start():
    uv.run("main:app", host="127.0.0.1", port=8000, reload=True)

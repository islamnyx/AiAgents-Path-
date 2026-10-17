import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()


app = FastAPI()

class AgentRequest(BaseModel):
    user_prompt: str



@app.get("/")
def read_root():
    return {"message": "Hello from my first AI agent backend!"}


"""
@app.get("/agent/{agent_name}")
def get_agent_status(agent_name: str):
    return {
        "agent": agent_name,
        "status": "online",
        "memory_loaded": True
    }
    """

@app.post("/ask-agent")
def ask_agent(request: AgentRequest):
    try:
        # Call the Gemini model (using gemini-2.5-flash as the standard fast model)
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=request.user_prompt,
        )
        
        return {
            "status": "success",
            "user_prompt": request.user_prompt,
            "agent_response": response.text
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

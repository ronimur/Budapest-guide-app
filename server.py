import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents import set_default_openai_key
from personas.orchestrator import ask_agents

key = os.environ.get("OPENAI_API_KEY")
if not key:
    raise ValueError("OPENAI_API_KEY not found in .env")
set_default_openai_key(key)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class ChatRequest(BaseModel):
    message: str
    lat: float | None = None
    lng: float | None = None


BASE_DIR = Path(__file__).parent

@app.get("/")
def index():
    return FileResponse(BASE_DIR / "index.html")


@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        results = await ask_agents(req.message, req.lat, req.lng)
        return {"agents": results}
    except Exception as e:
        import traceback
        print(f"Error: {e}", flush=True)
        traceback.print_exc()
        return {"error": str(e), "type": type(e).__name__}

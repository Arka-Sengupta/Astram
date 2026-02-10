from fastapi import FastAPI
from app.core import agent
from pydantic import BaseModel

app = FastAPI(title="Local AI Agent")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = agent.process_request(request.message)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000)

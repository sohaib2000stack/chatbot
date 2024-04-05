from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import chatbot  # Import the chatbot function directly

app = FastAPI(
    title="Chatbot API",
    version="1.0",
)

# CORS configuration
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/chatbot/")
async def run_chatbot(user_input: str):
    response = chatbot.chatbot(user_input)  # Call the chatbot function directly
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

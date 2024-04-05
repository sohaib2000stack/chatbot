from fastapi import FastAPI
from api.chatbot import router as chatbot_router
from fastapi.middleware.cors import CORSMiddleware

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

# Include the chatbot router
app.include_router(chatbot_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)














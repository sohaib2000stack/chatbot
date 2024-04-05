from fastapi import APIRouter

router = APIRouter()

@router.get("/chatbot")
async def run_chatbot(title: str):
    from api.chatbot import chatbot
    chatbot()
    return {"message": "Chatbot has been executed"(title)}

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from db import SessionLocal
from models import ChatUser, ChatSession, ChatMessage
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq
import os

# Load .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic input model
class ChatRequest(BaseModel):
    user_id: int
    message: str
    conversation_id: int | None = None

@app.post("/api/chat")
def chat(request: ChatRequest):
    db = SessionLocal()

    # Create or retrieve user
    user = db.query(ChatUser).filter_by(id=request.user_id).first()
    if not user:
        user = ChatUser(id=request.user_id)
        db.add(user)
        db.commit()

    # Handle session
    if request.conversation_id:
        session = db.query(ChatSession).filter_by(id=request.conversation_id).first()
    else:
        session = ChatSession(user_id=request.user_id, created_at=datetime.now())
        db.add(session)
        db.commit()

    # Call LLM (Groq)
    response = groq_client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": request.message}]
    )
    bot_reply = response.choices[0].message.content

    # Save messages
    db.add(ChatMessage(session_id=session.id, sender="user", message=request.message, timestamp=datetime.now()))
    db.add(ChatMessage(session_id=session.id, sender="bot", message=bot_reply, timestamp=datetime.now()))
    db.commit()

    return {"reply": bot_reply, "conversation_id": session.id}

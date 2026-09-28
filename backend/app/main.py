from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api import auth, leads, contacts, notes, tasks, analytics, ai

settings = get_settings()

app = FastAPI(
    title="TTP CRM API",
    description="Enterprise CRM — FastAPI + Supabase (converted from MERN)",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CLIENT_URL, "http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(leads.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")
app.include_router(notes.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
app.include_router(ai.router, prefix="/api")


@app.get("/api/health")
async def health():
    return {"success": True, "message": "API is running..."}
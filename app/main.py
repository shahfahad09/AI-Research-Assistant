from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import STATIC_DIR
from app.routes import web_routes, api_routes

app = FastAPI(
    title="AI Research Assistant",
    description="A RAG-based AI Research Assistant using FastAPI, ChromaDB, and Gemini API.",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

app.include_router(web_routes.router)
app.include_router(api_routes.router)
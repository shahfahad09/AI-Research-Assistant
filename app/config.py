import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

APP_DIR = BASE_DIR / "app"
UPLOAD_DIR = BASE_DIR / "uploads"
CHROMA_DIR = BASE_DIR / "chroma_db"

TEMPLATE_DIR = APP_DIR / "templates"
STATIC_DIR = APP_DIR / "static"

UPLOAD_DIR.mkdir(exist_ok=True)
CHROMA_DIR.mkdir(exist_ok=True)

GEMINI_MODEL = "gemini-2.5-flash"


def read_api_key():
    key = os.getenv("GEMINI_API_KEY")
    if key:
        return key

    env_path = BASE_DIR / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip()

    return None


GEMINI_API_KEY = read_api_key()

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")
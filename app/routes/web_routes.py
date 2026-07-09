from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import TEMPLATE_DIR, UPLOAD_DIR
from app.services.rag_service import process_uploaded_pdf, answer_question
from app.services.vector_store_service import count_documents, clear_collection

router = APIRouter()
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": None,
            "answer": None,
            "sources": None,
            "document_count": count_documents()
        }
    )


@router.post("/upload", response_class=HTMLResponse)
async def upload_pdf(request: Request, file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "message": "Only PDF files are supported.",
                "answer": None,
                "sources": None,
                "document_count": count_documents()
            }
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        result = process_uploaded_pdf(str(file_path), file.filename)
        message = result["message"]

    except Exception as e:
        error_text = str(e)

        if (
            "429" in error_text
            or "RESOURCE_EXHAUSTED" in error_text
            or "quota" in error_text.lower()
        ):
            message = (
                "⚠️ Embedding API quota exceeded.\n"
                "Please wait about one minute and try again.\n"
                "For larger PDFs, use a paid Gemini API key or reduce the chunk size."
            )
        else:
            message = f"Upload failed: {error_text}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": message,
            "answer": None,
            "sources": None,
            "document_count": count_documents()
        }
    )

@router.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    result = answer_question(question)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": None,
            "answer": result["answer"],
            "sources": result["sources"],
            "document_count": count_documents()
        }
    )


@router.post("/clear", response_class=HTMLResponse)
async def clear_database(request: Request):
    deleted_count = clear_collection()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": f"Database cleared successfully. {deleted_count} chunks deleted.",
            "answer": None,
            "sources": None,
            "document_count": count_documents()
        }
    )

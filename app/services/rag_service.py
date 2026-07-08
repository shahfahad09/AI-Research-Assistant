from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import split_text_into_chunks
from app.services.vector_store_service import store_chunks, retrieve_chunks
from app.services.gemini_service import generate_answer


def process_uploaded_pdf(file_path: str, filename: str):
    text = extract_text_from_pdf(file_path)

    if not text.strip():
        return {
            "success": False,
            "message": "No readable text found in PDF.",
            "chunks": 0
        }

    chunks = split_text_into_chunks(text)

    store_chunks(chunks, filename)

    return {
        "success": True,
        "message": f"PDF processed successfully. {len(chunks)} chunks stored.",
        "chunks": len(chunks)
    }


def answer_question(question: str):
    retrieved_chunks = retrieve_chunks(question)

    if not retrieved_chunks:
        return {
            "answer": "No relevant information found in the uploaded documents.",
            "sources": []
        }

    answer = generate_answer(question, retrieved_chunks)

    return {
        "answer": answer,
        "sources": retrieved_chunks
    }
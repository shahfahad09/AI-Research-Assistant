from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_answer(question: str, retrieved_chunks):
    context = "\n\n".join(
        [
            f"Source: {chunk['source']} | Chunk: {chunk['chunk_index']}\n{chunk['text']}"
            for chunk in retrieved_chunks
        ]
    )

    prompt = f"""
You are an AI Research Assistant.

Answer the user's question using ONLY the provided retrieved context.

If the answer is not available in the context, say:
"I could not find enough information in the uploaded documents."

User Question:
{question}

Retrieved Context:
{context}

Instructions:
- Give a clear and structured answer.
- Use bullet points where helpful.
- Mention source file name and chunk number.
- Do not hallucinate.
- Keep the answer professional.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text
import uuid
import chromadb

from app.config import CHROMA_DIR
from app.services.embedding_service import create_embedding

chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))

collection = chroma_client.get_or_create_collection(
    name="research_documents"
)


def store_chunks(chunks, filename: str):
    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for index, chunk in enumerate(chunks):
        ids.append(str(uuid.uuid4()))
        documents.append(chunk)
        embeddings.append(create_embedding(chunk))
        metadatas.append({
            "source": filename,
            "chunk_index": index
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )


def retrieve_chunks(question: str, top_k: int = 4):
    query_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    retrieved = []

    for doc, meta in zip(documents, metadatas):
        retrieved.append({
            "text": doc,
            "source": meta.get("source", "Unknown"),
            "chunk_index": meta.get("chunk_index", "N/A")
        })

    return retrieved


def count_documents():
    return collection.count()


def clear_collection():
    all_items = collection.get()
    ids = all_items.get("ids", [])

    if ids:
        collection.delete(ids=ids)

    return len(ids)
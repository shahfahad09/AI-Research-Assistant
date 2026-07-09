from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text_into_chunks(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2500,
        chunk_overlap=300
    )

    return splitter.split_text(text)

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text_into_chunks(full_text: str) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_text(full_text)

    return chunks
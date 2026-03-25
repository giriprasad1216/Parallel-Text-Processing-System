# chunker.py

def create_chunks(text, chunk_size=50):
    lines = text.split("\n")
    chunks = []

    for i in range(0, len(lines), chunk_size):
        chunk = " ".join(lines[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks
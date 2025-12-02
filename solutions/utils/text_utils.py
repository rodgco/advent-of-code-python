def split_into_chunks(text, chunks):
    chunk_size = len(text) // chunks
    result = split_into_chunks_bysize(text, chunk_size)
    if len(result) > chunks:
        raise ValueError(f"Expected at most {chunks} chunks, but got {len(result)}")
    return result

def split_into_chunks_bysize(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


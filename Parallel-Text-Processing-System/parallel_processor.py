from multiprocessing import Pool, cpu_count
from sentiment import analyze_sentiment

# worker function
def process_single_chunk(chunk):
    sentiment, score = analyze_sentiment(chunk)
    return (chunk, sentiment, score)

def process_chunks(chunks, workers=None):

    # configurable workers
    if workers is None:
        workers = cpu_count()

    with Pool(processes=workers) as pool:
        results = pool.map(process_single_chunk, chunks)

    return results
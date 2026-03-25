from sentiment_engine import analyze_sentiment
from datetime import datetime

def process_reviews(reviews):

    results = []

    for review in reviews:

        sentiment, score = analyze_sentiment(review)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        results.append({
            "Text": review,
            "Sentiment": sentiment,
            "Score": score,
            "Timestamp": timestamp
        })

    return results
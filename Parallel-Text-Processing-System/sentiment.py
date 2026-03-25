# sentiment.py

positive_words = ["good", "happy", "excellent", "great", "success"]
negative_words = ["bad", "sad", "poor", "failure", "problem"]

def analyze_sentiment(text):
    score = 0
    words = text.lower().split()

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, score
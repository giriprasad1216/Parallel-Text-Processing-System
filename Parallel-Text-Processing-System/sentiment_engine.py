# sentiment_engine.py

from datetime import datetime

def analyze_sentiment(text):

    positive_rules = {
        "good": 1, "excellent": 3, "amazing": 2, "happy": 2,
        "beautiful": 2, "nice": 1, "great": 2, "love": 2,
        "best": 3, "wonderful": 3, "awesome": 2, "fantastic": 3
    }

    negative_rules = {
        "bad": -1, "worst": -3, "error": -2, "poor": -2,
        "difficult": -2, "hard": -1, "problem": -2,
        "hate": -3, "boring": -2, "slow": -1, "fail": -2
    }

    words = text.lower().split()

    score = 0

    for i, word in enumerate(words):

        # Handle "not good"
        if word == "not" and i + 1 < len(words):
            next_word = words[i + 1]
            if next_word in positive_rules:
                score -= positive_rules[next_word]

        # Handle "very good"
        elif word == "very" and i + 1 < len(words):
            next_word = words[i + 1]
            if next_word in positive_rules:
                score += positive_rules[next_word] + 1

        # Normal words
        elif word in positive_rules:
            score += positive_rules[word]

        elif word in negative_rules:
            score += negative_rules[word]

    # Final sentiment
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return sentiment, score, timestamp
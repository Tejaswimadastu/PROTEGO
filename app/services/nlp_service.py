# app/services/nlp_service.py

from transformers import pipeline

# Load models once (on startup)
sentiment_model = pipeline("sentiment-analysis")
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

def analyze_text(text: str):
    """
    Analyze text using NLP models
    """

    sentiment_result = sentiment_model(text)[0]
    emotion_result = emotion_model(text)[0]

    return {
        "text": text,
        "sentiment": sentiment_result["label"],
        "sentiment_score": float(sentiment_result["score"]),
        "emotion": emotion_result["label"],
        "emotion_score": float(emotion_result["score"])
    }
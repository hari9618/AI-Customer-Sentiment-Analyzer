from transformers import pipeline
import streamlit as st


# -----------------------------
# Load Model
# -----------------------------

@st.cache_resource
def load_model():

    model = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    return model


model = load_model()


# -----------------------------
# Negation Words
# -----------------------------

NEGATIONS = [
    "not",
    "no",
    "never",
    "don't",
    "didn't",
    "isn't",
    "wasn't",
    "can't",
    "won't"
]


# -----------------------------
# Predict Sentiment
# -----------------------------

def predict_sentiment(text):

    if not text.strip():

        return "NEUTRAL", 0.0


    text_lower = text.lower()

    result = model(text)[0]

    label = result["label"]
    score = result["score"]


    sentiment = "POSITIVE" if label == "POSITIVE" else "NEGATIVE"


    # -----------------------------
    # NEGATION HANDLING
    # -----------------------------

    words = text_lower.split()

    for i, word in enumerate(words):

        if word in NEGATIONS and i+1 < len(words):

            next_word = words[i+1]

            if next_word in ["happy","good","great","satisfied","excellent"]:

                sentiment = "NEGATIVE"
                score = 0.90


    return sentiment, score


# -----------------------------
# AI Explanation
# -----------------------------

def explain_sentiment(text, sentiment):

    text_lower = text.lower()

    positive_words = [
        "good","great","excellent","amazing",
        "love","happy","satisfied","perfect"
    ]

    negative_words = [
        "bad","worst","poor","slow",
        "hate","problem","issue","delay"
    ]


    # NEGATION EXPLANATION
    if "not happy" in text_lower:
        return "The sentiment is negative because the phrase 'not happy' indicates dissatisfaction."

    if "not good" in text_lower:
        return "The feedback indicates the product or service was not good, leading to negative sentiment."

    if "not satisfied" in text_lower:
        return "The sentiment is negative because the customer mentioned they are not satisfied."


    # POSITIVE CASE
    if sentiment == "POSITIVE":

        words = [w for w in positive_words if w in text_lower]

        if words:

            return f"The sentiment is positive because the feedback contains positive words such as: {', '.join(words)}."

        return "The AI model detected a positive tone and customer satisfaction."


    # NEGATIVE CASE
    if sentiment == "NEGATIVE":

        words = [w for w in negative_words if w in text_lower]

        if words:

            return f"The sentiment is negative because the feedback contains words such as: {', '.join(words)}."

        return "The sentiment appears negative as the feedback expresses dissatisfaction with the experience."


    return "Neutral sentiment detected."
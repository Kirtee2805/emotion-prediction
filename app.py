import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("emotion_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Emotion labels
emotion_labels = {
    0: "sadness",
    1: "anger",
    2: "love",
    3: "surprise",
    4: "fear",
    5: "joy"
}

# Emotion emojis
emotion_emojis = {
    "sadness": "😢",
    "anger": "😡",
    "love": "❤️",
    "surprise": "😲",
    "fear": "😨",
    "joy": "😄"
}

# Page settings
st.set_page_config(
    page_title="Emotion Predictor",
    page_icon="😊",
    layout="centered"
)

# Header
st.title("😊 Emotion Predictor")
st.markdown("### Predict emotions from text using NLP ")

st.write("---")

# User Input
user_text = st.text_area(
    "Enter your text",
    placeholder="Example: I am very happy today!",
    height=150
)

# Predict Button
if st.button("🔍 Predict Emotion"):

    if user_text.strip():

        # Transform text
        text_vector = tfidf.transform([user_text])

        # Predict
        prediction = model.predict(text_vector)[0]

        # Convert number to emotion
        emotion = emotion_labels.get(int(prediction), "Unknown")

        # Get emoji
        emoji = emotion_emojis.get(emotion, "🤖")

        # Show result
        st.success(f"{emoji} Predicted Emotion: {emotion.upper()}")

    else:
        st.warning("⚠️ Please enter some text.")

st.write("---")
st.caption("Built using Streamlit, TF-IDF Vectorizer and Logistic Regression")
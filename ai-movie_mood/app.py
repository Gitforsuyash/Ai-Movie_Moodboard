import streamlit as st
from transformers import pipeline
import os

# Page configuration
st.set_page_config(page_title="🎬 AI Movie Moodboard", layout="centered")

# Title and description
st.title("🎞️ AI-Powered Movie Moodboard")
st.markdown("Describe your movie's plot or vibe. Let AI visualize its emotion with a moodboard!")

# Load emotion classification model
@st.cache_resource
def load_emotion_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

emotion_classifier = load_emotion_model()

# Detect emotion from text

def detect_emotion(text):
    try:
        result = emotion_classifier(text)
        st.write("🔍 Raw Emotion Output:", result)  # Debug
        # Check the nested list structure before accessing
        if result and isinstance(result, list) and result[0] and isinstance(result[0], list) and result[0][0] and 'label' in result[0][0]:
            return result[0][0]['label'].lower() # <-- THE FIX IS HERE
        else:
            return "unknown"
    except Exception as e:
        st.error(f"Error during emotion detection: {e}")
        return "unknown"

# Text input
description = st.text_area("📝 Describe your movie plot or emotional vibe here:", height=150)

if description:
    with st.spinner("🔍 Analyzing emotion..."):
        emotion = detect_emotion(description)
        st.success(f"✅ Detected Emotion: **{emotion.capitalize()}**")

    st.subheader("🖼️ Moodboard")

    # Set image folder path
    image_dir = os.path.join("emotions", emotion)

    if not os.path.isdir(image_dir) or not os.listdir(image_dir):
        st.warning(f"No images found for **{emotion}**.\nPlease add images to `emotions/{emotion}/`.")
    else:
        for image_file in os.listdir(image_dir):
            image_path = os.path.join(image_dir, image_file)
            st.image(image_path, use_container_width=True)

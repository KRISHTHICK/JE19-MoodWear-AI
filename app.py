import streamlit as st
from mood_agent import detect_mood, generate_caption
from outfit_utils import recommend_outfit

st.set_page_config(page_title="MoodWear AI", layout="wide")
st.title("🧘‍♀️👕 MoodWear AI – Mood-Based Outfit Recommender")

st.markdown("Tell us how you’re feeling today, and we’ll build a mood-aligned look for you!")

user_input = st.text_input("How are you feeling today?")
weather = st.selectbox("Select today's weather:", ["Sunny", "Cloudy", "Rainy", "Cold", "Hot"])
event = st.selectbox("What's the occasion?", ["Work", "Casual", "Date", "Party", "Travel"])

if user_input:
    mood = detect_mood(user_input)
    st.success(f"Detected Mood: **{mood}**")

    st.subheader("👗 Recommended Outfit:")
    outfit = recommend_outfit(mood, weather, event)
    st.markdown(outfit)

    st.subheader("📸 Instagram Caption:")
    st.text_area("Caption:", generate_caption(mood, event), height=150)

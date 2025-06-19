# JE19-MoodWear-AI
Gen Ai

🧘‍♀️👕 MoodWear AI – AI-Powered Mood-Based Outfit Recommender
🧠 Project Concept:
MoodWear AI is an AI stylist agent that recommends outfits based on a user’s mood, weather, and calendar events. It uses a combination of sentiment analysis, local LLMs via Ollama, and fashion logic to create personalized outfit ideas, Instagram captions, and even recommends accessories/colors.

🌟 Key Features:
Feature	Description
😌 Mood Detection Agent	User types how they feel → AI detects mood using sentiment analysis
🌤️ Weather-Based Adjustments	Takes live weather (mock or actual) into account to suggest weather-fit fashion
🗓️ Event-Aware Outfit Planning	Suggests outfits based on calendar event (e.g., Date, Office, Party)
🎨 Color Psychology Matching	Suggests colors based on mood and fashion theory
✍️ Caption & Hashtag Generator	Creates mood-aligned social media captions using Ollama
🛍️ Accessory Recommendations	Suggests shoes, bags, and more to enhance the full look

# 🧘‍♀️👕 MoodWear AI – Mood-Based Outfit Recommender

MoodWear AI is a fashion-tech AI project that recommends outfits based on user mood, weather, and event using local LLMs like TinyLLaMA.

## 🚀 Features
- Mood detection using sentiment analysis
- Smart outfit suggestions
- Instagram caption generation via Ollama
- Context-aware fashion planning

## 💻 How to Run

```bash
git clone https://github.com/yourusername/MoodWear-AI.git
cd MoodWear-AI
pip install -r requirements.txt
ollama run tinyllama
streamlit run app.py

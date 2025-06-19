from textblob import TextBlob
import subprocess

def detect_mood(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.3:
        return "Happy"
    elif polarity < -0.3:
        return "Sad"
    else:
        return "Neutral"

def generate_caption(mood, event):
    prompt = f"Generate a stylish Instagram caption for someone feeling {mood} going to a {event}."
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()

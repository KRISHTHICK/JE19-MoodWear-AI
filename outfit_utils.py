def recommend_outfit(mood, weather, event):
    recommendations = {
        ("Happy", "Sunny", "Casual"): "Flowy floral dress with sandals and a straw hat 🌻",
        ("Sad", "Rainy", "Work"): "Grey trench coat with black boots and a warm scarf ☔",
        ("Neutral", "Cold", "Date"): "Beige overcoat, skinny jeans, and burgundy boots 💖",
        ("Happy", "Hot", "Party"): "Bright crop top with denim shorts and statement earrings 🔥",
    }
    return recommendations.get((mood, weather, event), "Classic jeans, comfy tee, and a light jacket 👕")

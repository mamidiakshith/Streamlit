import streamlit as st
import random

# Sample restaurant data
restaurants = {
    "Hyderabad": {
        "Indian": ["Bawarchi", "Paradise Biryani", "Chutneys", "Shah Ghouse", "Ulavacharu"],
        "Chinese": ["Mainland China", "Haka", "Wok Republic", "Chopsticks", "China Bistro"],
        "Italian": ["Little Italy", "Olive Bistro", "Flechazo", "Prego", "Via Milano"]
    },
    "Bangalore": {
        "Indian": ["Nagarjuna", "MTR", "Byg Brewski", "Karavalli", "Central Tiffin Room"],
        "Chinese": ["Beijing Bites", "Wangs Kitchen", "Shao", "Szechwan Court", "Yauatcha"],
        "Italian": ["Toit", "Truffles", "Brik Oven", "Chianti", "Toscano"]
    },
    "Chennai": {
        "Indian": ["Murugan Idli Shop", "Copper Chimney", "Annachi", "A2B", "Kumar Mess"],
        "Chinese": ["The Cascade", "Mainland China", "Peking Palace", "Golden Dragon", "China Town"],
        "Italian": ["Tuscana", "Little Italy", "The Pasta Bar Veneto", "That Madras Place", "Benvenuto"]
    },
    "Delhi": {
        "Indian": ["Karim’s", "Gulati", "Rajinder Da Dhaba", "Bukhara", "Sita Ram Diwan Chand"],
        "Chinese": ["Berco’s", "Momo’s Point", "House of Ming", "Wow! Momo", "China Garden"],
        "Italian": ["Big Chill", "Diggin", "Artusi", "Jamie’s Italian", "Sorrento"]
    },
    "Mumbai": {
        "Indian": ["Gajalee", "Highway Gomantak", "Shree Thaker Bhojanalay", "Trishna", "Delhi Darbar"],
        "Chinese": ["China Gate", "Hakkasan", "5 Spice", "Mainland China", "Ling's Pavilion"],
        "Italian": ["Pizza By The Bay", "Little Italy", "Quattro", "Café Zoe", "Gustoso"]
    }
}

# App title
st.title("🍽️ Restaurant Recommendation App")

# User inputs
location = st.selectbox("📍 Choose your location:", list(restaurants.keys()))
cuisine = st.selectbox("🍜 Choose a cuisine:", list(restaurants[location].keys()))

# Recommend a restaurant
if st.button("Recommend"):
    choice = random.choice(restaurants[location][cuisine])
    st.success(f"✅ Try **{choice}** for delicious {cuisine} food in {location}!")

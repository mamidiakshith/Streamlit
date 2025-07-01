import streamlit as st
import random

movies = {
    "Happy": ["Zindagi Na Milegi Dobara", "Yeh Jawaani Hai Deewani", "3 Idiots"],
    "Sad": ["Tamasha", "October", "The Lunchbox"],
    "Excited": ["Dhoom 2", "War", "Pathaan"],
    "Romantic": ["Dilwale Dulhania Le Jayenge", "Kal Ho Naa Ho", "Aashiqui 2"]
}

st.title("🎬 Movie Recommendation")

mood = st.selectbox("💭 How are you feeling?", list(movies.keys()))

if st.button("🍿 Recommend Movie"):
    suggestion = random.choice(movies[mood])
    st.success(f"🎥 Watch *{suggestion}* to match your *{mood}* mood!")

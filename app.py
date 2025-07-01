import streamlit as st
import random

# Movie dataset organized by mood and genre
movie_db = {
    "Happy": {
        "Comedy": [
            ("Zindagi Na Milegi Dobara", "A fun road trip adventure of friendship and self-discovery."),
            ("3 Idiots", "An uplifting story about friendship, pressure, and success."),
            ("Chhichhore", "A nostalgic ride through college memories and life lessons.")
        ],
        "Romance": [
            ("Yeh Jawaani Hai Deewani", "A coming-of-age story with friendship and romance."),
            ("Dil Chahta Hai", "Three friends navigate love, life, and adulthood.")
        ]
    },
    "Sad": {
        "Drama": [
            ("Tamasha", "A journey of finding oneself beyond societal labels."),
            ("October", "A sensitive portrayal of love and loss."),
            ("The Lunchbox", "A beautiful accidental love story via lunchbox exchanges.")
        ],
        "Romance": [
            ("Aashiqui 2", "A musical love story with emotional depth."),
            ("Kal Ho Naa Ho", "Love, sacrifice, and heartbreak in one.")
        ]
    },
    "Excited": {
        "Action": [
            ("Dhoom 2", "High-octane stunts and stylish action."),
            ("War", "Spy thriller with intense action and twists."),
            ("Pathaan", "An Indian spy action blockbuster.")
        ],
        "Thriller": [
            ("Baby", "An elite counter-intelligence team fights terrorism."),
            ("Special 26", "A thrilling heist drama based on true events.")
        ]
    },
    "Romantic": {
        "Classic": [
            ("Dilwale Dulhania Le Jayenge", "An all-time romantic favorite."),
            ("Hum Aapke Hain Koun..!", "A grand love story in a traditional setting.")
        ],
        "Modern": [
            ("Jab We Met", "Two strangers meet and change each other's lives."),
            ("Barfi!", "An unconventional and heartwarming romantic tale.")
        ]
    }
}

# Session storage for recommendation history
if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("🎬 MovieSense – Your Mood-Based Movie Recommender")

st.markdown("Tell us your **mood** and preferred **genre**, and we'll suggest a perfect movie for you! 🍿")

# Mood and genre selection
mood = st.selectbox("💭 What's your mood today?", list(movie_db.keys()))

genre = st.selectbox("🎭 Choose a genre:", list(movie_db[mood].keys()))

if st.button("🎯 Recommend a Movie"):
    movie, description = random.choice(movie_db[mood][genre])
    st.session_state["history"].append(movie)

    st.success(f"🎥 **{movie}**")
    st.write(f"📝 *{description}*")
    
    st.image("https://source.unsplash.com/800x450/?cinema,movie", caption="Enjoy your show! 🍿")

# Show history of recommended movies
if st.session_state["history"]:
    with st.expander("📜 Your Recommendations History"):
        for idx, mv in enumerate(st.session_state["history"], 1):
            st.markdown(f"{idx}. 🎬 **{mv}**")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit by [Akshith...].")

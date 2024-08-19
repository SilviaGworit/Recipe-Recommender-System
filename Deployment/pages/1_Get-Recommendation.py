import streamlit as st
import pickle

# Title and description
st.title("🍽️ Recipe Recommender System")
st.write("Struggling to decide what to cook with the ingredients you have? Let our recommender system help you discover new recipes tailored just for you!")

# User inputs
st.header("Input Your Ingredients")
ingredients = st.text_input("Enter ingredients you have (e.g., 'tomatoes, chicken, basil')")


# Footer
st.write("---")
st.write("🔧 Developed with love 💟")

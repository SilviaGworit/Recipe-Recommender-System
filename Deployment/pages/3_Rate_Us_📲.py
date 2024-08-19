import streamlit as st

# Slider for feedback rating
feedback = st.slider('How much would you rate this app?', min_value=0, max_value=5, step=1)

# Check if feedback is provided
if feedback:
    st.header("Thank you for rating the app!")
else:
    st.write("Rate us with 💙")

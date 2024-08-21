import streamlit as st

# Contact Us page content
st.title("Contact Us 📞")

st.subheader("We'd Love to Hear From You!")

st.write("""
If you have any questions, feedback, or just want to say hello, feel free to reach out to us. We're here to help you make the most of your cooking experience!
""")

# Contact information
st.write("**Email:** support@recipeapp.com")
st.write("**Phone:** +254-123-456-789")
st.write("**Address:** Moringa, Westlands")

# Contact form
st.write("Or fill out the form below, and we'll get back to you as soon as possible:")

# Form inputs
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

# Submit button
if st.button("Submit"):
    # Placeholder action for form submission
    st.write(f"Thank you, {name}! We've received your message and will get back to you at {email}.")

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["FAQs", "Upcoming events 🎭"])
tab1.write("For General enquiries, Please contact support@recipeapp.com for any queries")
tab2.write("We'll definately update you of any upcoming Food Events ✅")

# Footer
st.write("---")
st.write("🔧 Developed with love 💟")

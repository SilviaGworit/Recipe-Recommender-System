import streamlit as st
import os

# Page setup
st.set_page_config(page_title="Hello")
st.sidebar.success("Have Fun & Don't forget to rate us.")

# Welcome page content
st.title("DATA CRUNCH ~ WEB APP")
st.header("Welcome to Your Personalized Recipe Recommender! 🍳")

st.subheader("Discover Delightful Meals with What You Have!")

st.write("""
Ready to transform your kitchen into a culinary playground? Whether you’re a seasoned chef or just looking to whip up something quick and tasty, our app is here to help. Discover delicious recipes tailored to the ingredients you already have on hand. Let’s make cooking fun and easy!""")


# Base directory
base_dir = os.path.dirname(os.path.dirname(__file__))

# Define the paths to the images using relative paths
image_path1 = os.path.join(base_dir, 'Deployment\Image', 'pic1.jpg')
image_path2 = os.path.join(base_dir, 'Deployment\Image', 'pic2.jpg')

# cols.
col1, col2 = st.columns(2)

col1.header("#Yummy")
col1.image(image_path1, caption="Delicious Recipes Just for You!", use_column_width=True)

col2.header("#Exquisite")
col2.image(image_path2, caption="Delicious Recipes Just for You!", use_column_width=True)

# Additional content
st.write("""
**Why Choose Us?**
- **✔️ Personalized Recommendations**
- **✔️ Catering to Your Needs**
- **✔️ Reduce Food Waste**
""")

st.write("""
**How It Works:**
1. **Enter Your Ingredients**: Input the ingredients you have, and our smart system will do the rest.
2. **Get Cooking**: Receive a list of recipes you can make right now and start cooking!
""")

st.write("""
We believe that cooking should be easy, fun, and stress-free. So go ahead, explore new recipes, try out new ingredients, and enjoy the process of creating delicious meals with what’s already in your kitchen.
""")

# Footer
st.write("---")
st.write("🔧 Developed with love 💟")

import streamlit as st

# Page setup
st.set_page_config(page_title="Hello")
st.sidebar.success("Have Fun & Don't forget to rate us.")

# Welcome page content
st.title("Welcome to Your Personalized Recipe Recommender! 🍳")

st.subheader("Discover Delightful Meals with What You Have!")

st.write("""
Welcome to our Recipe Recommender System, where we turn your kitchen into a culinary adventure. Whether you’re a seasoned chef or just looking to whip up something quick and easy, our app is here to help you discover delicious recipes tailored to the ingredients you already have.
""")

# Displaying images correctly
col1, col2 = st.columns(2)

# Load images from file paths
col1.header(".")
col1.image("Image/pic1.jpg", caption="Delicious Recipes Just for You!", use_column_width=True)

col2.header(".")
col2.image("Image/pic2.jpg", caption="Delicious Recipes Just for You!", use_column_width=True)

# Additional content
st.write("""
**Why Choose Us?**
- **Personalized Recommendations**: Just enter the ingredients you have at home, and we'll suggest recipes that match. No more last-minute grocery runs!
- **Catering to Your Needs**: Whether you're vegetarian, vegan, gluten-free, or have other dietary preferences, we’ve got you covered with recipes that suit your lifestyle.
- **Reduce Food Waste**: Use up what you have in your pantry and fridge, and create amazing meals without wasting food.
""")

st.write("""
**How It Works:**
1. **Enter Your Ingredients**: Input the ingredients you have, and our smart system will do the rest.
2. **Set Your Preferences**: Choose any dietary restrictions or preferences.
3. **Get Cooking**: Receive a list of recipes you can make right now and start cooking!
""")

st.write("""
We believe that cooking should be easy, fun, and stress-free. So go ahead, explore new recipes, try out new ingredients, and enjoy the process of creating delicious meals with what’s already in your kitchen.
""")

# Footer
st.write("---")
st.write("🔧 Developed with love 💟")

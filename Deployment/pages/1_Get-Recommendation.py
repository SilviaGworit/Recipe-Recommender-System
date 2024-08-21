import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from difflib import get_close_matches

# Define paths to your files
tfidf_path = 'C:/Users/ADMIN/Desktop/Notebook Folder/CAPSTONE PROJECT/Recipe-Recommender-System/tfidf_model.pkl'
svd_model_path = 'C:/Users/ADMIN/Desktop/Notebook Folder/CAPSTONE PROJECT/Recipe-Recommender-System/model.pkl'
recipe_lsa_path = 'C:/Users/ADMIN/Desktop/Notebook Folder/CAPSTONE PROJECT/Recipe-Recommender-System/recipe_lsa.pkl'
recipe_data_path = 'C:/Users/ADMIN/Desktop/Notebook Folder/CAPSTONE PROJECT/Recipe-Recommender-System/Deployment/data_deploy.csv'


# Load pre-trained models
tfidf = joblib.load(tfidf_path)
svd_model = joblib.load(svd_model_path)
recipe_lsa = joblib.load(recipe_lsa_path) 

# Load recipe data
data = pd.read_csv(recipe_data_path)  
all_ingredients = data['ingredients'].str.split(',').explode().str.strip().unique()

# Preprocess ingredients
def preprocess_ingredients(ingredients):
    return ','.join(sorted(set(ingredient.strip().lower() for ingredient in ingredients.split(','))))

def spell_check_ingredients(input_ingredients, all_ingredients):
    corrected_ingredients = []
    for ingredient in input_ingredients.split(','):
        ingredient = ingredient.strip().lower()
        matches = get_close_matches(ingredient, all_ingredients, n=1, cutoff=0.6)
        if matches:
            corrected_ingredients.append(matches[0])
        else:
            corrected_ingredients.append(ingredient)
    return ','.join(corrected_ingredients)

def get_recipe_recommendations(input_ingredient, tfidf, svd_model, recipe_lsa, data):
    processed_input = preprocess_ingredients(input_ingredient)
    input_tfidf = tfidf.transform([processed_input])
    input_lsa = svd_model.transform(input_tfidf)
    cosine_sim = cosine_similarity(input_lsa, recipe_lsa).flatten()
    data['similarity_score'] = cosine_sim
    recommendations = data.drop_duplicates(subset=['recipe_name'])
    recommendations = recommendations.sort_values(by='similarity_score', ascending=False)
    return recommendations

# Streamlit interface
st.title("🍽️ Recipe Recommender System")
st.write("Struggling to decide what to cook with the ingredients you have? Let our recommender system help you discover new recipes tailored just for you!")

# User inputs
st.header("Input Your Ingredients")
ingredients = st.text_input("Enter ingredients you have (e.g., 'tomatoes, chicken, basil')")

if ingredients:
    recommendations = get_recipe_recommendations(ingredients, tfidf, svd_model, recipe_lsa, data)
    if not recommendations.empty:
        st.write("### Top 5 Recommended Recipes:")
        for i, (_, row) in enumerate(recommendations.head(5).iterrows(), 1):
            st.write(f"**{i}. {row['recipe_name']}** (Rating: {row['ratings']:.2f}, Similarity: {row['similarity_score']:.2f})")
            st.write(f"Ingredients: {row['ingredients']}")
            st.write(f"Cooking Instructions: {row['cooking_instructions'][:100]}...")  # Truncated for brevity
            if st.button(f"Show full instructions for recipe {i}"):
                st.write(row['cooking_instructions'])

    else:
        st.write("Sorry, no recipes found with those ingredients. Try adding more ingredients or using more common ones.")

# Footer
st.write("---")
st.write("🔧 Developed with love 💟")

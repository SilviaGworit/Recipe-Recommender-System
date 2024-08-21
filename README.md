# Recipe Recommender System

## Contributors
- Silvia Gworit
- Denis Mwenda
- Myra Kadenge
- Paul Muniu
- Ian Nzangi

## Overview
Tech to Tech Hub, in collaboration with Flavor Fields, developed an innovative recipe recommendation system called **Data Crunch**. This application provides personalized recipe suggestions based on the ingredients users have at their disposal, catering to various dietary preferences and meal categories.

## Problem Statement
Many people face the challenge of having various ingredients in their kitchen but struggle to decide what to cook. This leads to either time-consuming meal preparation or the need to purchase additional ingredients. The overwhelming number of recipe options can make meal planning daunting. **Data Crunch** addresses these challenges by offering personalized recipe suggestions, reducing food waste, and simplifying meal planning.

## Objectives
1. **Main Objective:** Develop an interactive, user-friendly recommender system that provides personalized recipe suggestions based on user-input ingredients.
2. **Recipe Matching:** Implement an algorithm that matches user-input ingredients with a comprehensive recipe database to offer tailored recipe suggestions.
3. **User Interface and Experience Design:** Create an intuitive and user-friendly interface allowing users to easily browse recipes, read reviews, and receive personalized suggestions.

## Datasets
We utilized two main datasets for this project:
1. **Recipe Review and User Feedback Dataset (from UCI):** This dataset includes details such as recipe number, recipe name, user information (ID, name, reputation), review details (created at, reply count, thumbs up/down, stars, best score), and comment text.
2. **Ingredients Dataset (from Kaggle):** This dataset includes recipe names, ingredients lists, and cooking instructions.

## Methodology
### CRISP-DM Process
1. **Business Understanding:** Defined the project's goals and objectives.
2. **Data Understanding:** Analyzed the datasets to understand their structure and content.
3. **Data Preparation:** Cleaned and preprocessed the data to make it suitable for modeling.
4. **Modeling:** Experimented with several models, including K-Nearest Neighbors (KNN) and Singular Value Decomposition (SVD), to develop the recommendation system.
5. **Evaluation:** The models were evaluated based on their performance, with the Tuned SVD Model being the best-performing model.
6. **Deployment:** Deployed the model using Streamlit to create an interactive web application.

# Recipe Data Analysis

## Overview
This project involves the analysis of recipe data, focusing on understanding user preferences, satisfaction levels, and popular recipes. The data was collected from user reviews and recipe details, and several exploratory data analysis (EDA) techniques were employed to gain insights.

## Top Ingredients
input image here

The above graph shows the most frequently used ingredients in the dataset. Savory ingredients are the most common, indicating a strong preference for savory dishes among users.

## Distribution of Ratings
input image here

This graph illustrates the distribution of user ratings for the recipes. The majority of ratings are 5 stars, which indicates high user satisfaction. However, there are also notable counts of 0-star and 4-star ratings.

## Top Recipes
input image here

The top recipes graph represents the most popular recipes based on user ratings. These recipes are the favorites among users and have received the highest ratings in the dataset.

## Conclusion
The insights derived from the EDA can be used to enhance recipe recommendations and improve user experience by focusing on popular ingredients and recipes, as well as addressing areas where user satisfaction is lower.



### Key Results
- The **Tuned SVD Model** had the best performance, with a Root Mean Squared Error (RMSE) of 1.5374 and a Mean Absolute Error (MAE) of 1.0629.
- The system suggests recipes based on predicted ratings and user input, allowing users to select their preferred recipes and receive cooking instructions.

## User Interface and Deployment
The **Data Crunch** web application was built using Streamlit, providing a user-friendly interface for users to input ingredients and receive recipe recommendations. The app was deployed using Streamlit Community Cloud, enabling easy collaboration and sharing.

## Recommendations for Future Work
- **Recipe Categorization:** Develop a robust categorization system that classifies recipes based on cuisines, ingredients, cooking methods, and dietary preferences. Incorporate a diverse range of cuisines to cater to a broad audience.
- **Automated Sentiment Analysis:** Implement automated sentiment analysis to analyze user feedback in real-time. Use NLP techniques to extract insights from reviews and adjust recommendations accordingly.


## Conclusion
The **Data Crunch** system successfully provides personalized recipe recommendations, simplifying the meal planning process and enhancing the cooking experience.

---

Thank you for using Data Crunch! For any questions, feel free to reach out to our team.

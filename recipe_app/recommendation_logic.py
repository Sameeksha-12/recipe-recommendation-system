# recommendation_logic.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_recipes(user_cuisine, user_diet, user_ingredients, user_course):
    # Load data from CSV file
    data_file = 'final_dataset.csv'
    recipe_data = pd.read_csv(data_file)

    # Filter recipes based on user preferences
    filtered_recipes = recipe_data[(recipe_data['cuisine'] == user_cuisine) &
                                   (recipe_data['diet'] == user_diet) &
                                   (recipe_data['course'] == user_course)]

    if filtered_recipes.empty:
        print("No matching recipes found. Please try different preferences.")
        return None

    # Create TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_recipes['full_text'])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Perform recommendation based on user input
    # Example code to get top 5 similar recipes
    user_input_text = ' '.join(user_ingredients)
    user_input_vector = tfidf_vectorizer.transform([user_input_text])
    cosine_similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    top_indices = cosine_similarities.argsort()[0][-5:][::-1]
    recommended_recipes = filtered_recipes.iloc[top_indices][['name', 'description','ID']]

    return recommended_recipes

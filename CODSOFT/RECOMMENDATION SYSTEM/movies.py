import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie ratings data
data = {
    'user_id': ['1', '1', '1', '2', '2', '3', '3', '4', '4', '4', '5', '5', '5', '5'],
    'item_name': ['Baahubali: The Beginning', 'Baahubali 2: The Conclusion', 'Rangasthalam', 'Ala Vaikunthapurramuloo', 'Arjun Reddy', 'Bheeshma', 'Jersey', 'Geetha Govindam', 'Mahanati', 'Srimanthudu', 'F2: Fun and Frustration', 'Eega', 'Nannaku Prematho', 'Attarintiki Daredi'],
    'rating': [9, 7, 6, 8, 7, 8, 9, 6, 9, 7, 8, 8, 7, 6]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Create a user-item matrix with movie names as columns
user_item_matrix = df.pivot_table(index='user_id', columns='item_name', values='rating', fill_value=0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get movie recommendations for a new user
def get_recommendations(new_user_ratings, user_similarity_df, user_item_matrix, n_recommendations=5):
    # Add new user ratings to the user-item matrix
    new_user_id = str(len(user_item_matrix) + 1)
    new_user_df = pd.DataFrame(new_user_ratings, index=[new_user_id])
    user_item_matrix = pd.concat([user_item_matrix, new_user_df], axis=0)
    user_item_matrix.fillna(0, inplace=True)

    # Update user similarity matrix
    user_similarity = cosine_similarity(user_item_matrix)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

    # Get the similarity scores for the new user
    sim_scores = user_similarity_df.loc[new_user_id]

    # Calculate weighted ratings for all movies
    weighted_ratings = user_item_matrix.T.dot(sim_scores)
    weighted_ratings = weighted_ratings / sim_scores.sum()

    # Drop movies that the new user has already rated
    rated_movies = new_user_df.columns[new_user_df.loc[new_user_id] > 0].tolist()
    weighted_ratings = weighted_ratings.drop(labels=rated_movies)

    # Sort the ratings in descending order and return the top N recommendations
    recommendations = weighted_ratings.sort_values(ascending=False).head(n_recommendations)
    return recommendations

# New user ratings (this is where you input the new user's ratings)
new_user_ratings = {
    'Baahubali: The Beginning': 7,
    'Baahubali 2: The Conclusion': 8
}

# Get movie recommendations
recommendations = get_recommendations(new_user_ratings, user_similarity_df, user_item_matrix)
print("Recommended Movies for the New User:")
print(recommendations)

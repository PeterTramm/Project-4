from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split  # Add this line
from sklearn.neighbors import NearestNeighbors  # Add this line
import random

app = Flask(__name__)

# Load the movie dataset
movies_file_path = 'Resources/tmdb_movies_list.csv'
df_movies = pd.read_csv(movies_file_path)

# Compute TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_movies['Plot'])

# Compute cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to compute recommendations
def nearest_neigh_model_genre(title, element, cosine_sim=cosine_sim):
    # Filter DataFrame by movie title
    filtered_movies = df_movies[df_movies['Title'] == title]
    
    # Check if any rows match the specified title
    if filtered_movies.empty:
        return "Movie title not found in database", []
    
    # Get the index of the movie that matches the title
    idx = filtered_movies.index[0]
    
    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Take the cosine similarity scores of all the movies 
    second_elements = [x[1] for x in sim_scores]
    
    # Set up tfidf on the plot column 
    X = df_movies['Plot']
    X_tfidf = tfidf.fit_transform(X)
    
    # Use the cosine similarity score as y
    y = second_elements
    
    X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.5, random_state=42
    )
    
    neigh = NearestNeighbors(n_neighbors=2, radius=0.4)
    neigh.fit(X_tfidf)
    
    movie_indices = []
    for i in neigh.kneighbors(X_tfidf[idx], 11, return_distance=False)[0][1:]:
        movie_indices.append(i)
    
    # Get the details of recommended movies including poster URLs
    recommended_movies = df_movies.iloc[movie_indices][['Title', 'Poster', 'Plot']].to_dict(orient='records')
    
    return "", recommended_movies


# Function to get random movies from similar movies (indices 11 to 50)
def get_random_movies(num_movies):
    # Get similar movie indices from 11 to 50
    similar_movie_indices = range(11, 51)
    # Randomly select num_movies from similar movie indices
    random_indices = random.sample(similar_movie_indices, num_movies)
    # Get the details of randomly selected movies
    random_movies = df_movies.iloc[random_indices][['Title', 'Poster', 'Plot']].to_dict(orient='records')
    return random_movies

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form and convert to lowercase
        movie_title = request.form['movie_title'].lower()
        
        # Filter DataFrame by movie titles and convert titles to lowercase for case-insensitive comparison
        filtered_movies = df_movies[df_movies['Title'].str.lower() == movie_title]
        
        # Check if any rows match the specified title
        if filtered_movies.empty:
            message = "Movie title not found in database"
            recommended_movies = []
        else:
            # Get the index of the first matching movie title
            idx = filtered_movies.index[0]

            # Get the pairwsie similarity scores of all movies with that movie
            sim_scores = list(enumerate(cosine_sim[idx]))

            # Sort the movies based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the 10 most similar movies
            sim_scores = sim_scores[1:11]

            # Get the movie indices
            movie_indices = [i[0] for i in sim_scores]
            
            # Get the recommended movies with their poster URLs
            recommended_movies = df_movies.iloc[movie_indices][['Title', 'Poster', 'Plot']].to_dict(orient='records')
            message = ""
        
        # Get random movies
        random_movies = get_random_movies(20)
        
        return render_template('index.html', message=message, recommended_movies=recommended_movies, random_movies=random_movies)
    else:
        return render_template('index.html', message="", recommended_movies=[], random_movies=[])

if __name__ == '__main__':
    app.run(debug=True)
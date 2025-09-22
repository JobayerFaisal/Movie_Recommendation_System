import streamlit as st
import pickle
import pandas as pd
import requests
import zipfile
import numpy as np

# Fatching poster from API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
# fetcjh poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters



# Function to load .pkl files from the zip archive
def load_pkl_files_from_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()  # Extracts the files to the current directory
        print("Extracted files:", zip_ref.namelist())
        
        # Load the movie_dict.pkl file
        with open(zip_ref.namelist()[0], 'rb') as f:
            movies_dict = pickle.load(f)
        # Load the similarity.pkl file
        with open(zip_ref.namelist()[1], 'rb') as f:
            similarity = pickle.load(f)
    
    return movies_dict, similarity

# Load movie data and similarity data
movies_dict, similarity = load_pkl_files_from_zip('models.zip')
#movies_dict = pickle.load(open('movie_dict.zip'))
#similarity = pickle.load(open('similarity.zip'))
movies = pd.DataFrame(movies_dict)



# Streamlit UI

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie you like',  
    movies['title'].values)


# When the button is clicked, call the recommend function and display the results
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])
#streamlit run app.py


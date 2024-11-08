import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = Similarity[movie_index]
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = []
    recommended_movies_poster = []

    for i in movies_list2:
        recommendations.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].id))
    return recommendations, recommended_movies_poster
def fetch_poster(movie_id):
    import requests

    url = "https://api.themoviedb.org/3/movie/{}?api_key=40d7bc4903fe5660b4968306760b6846".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer 40d7bc4903fe5660b4968306760b6846"
    }
    response = requests.get(url, headers=headers)
    data =  response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender')
option = st.selectbox('Movies List', movies['title'].values)
Similarity = pickle.load(open('Similarity.pkl', 'rb'))
if st.button('Recommend'):
    recommendations, posters = recommend(option)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])






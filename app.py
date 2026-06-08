import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

# ── Download similarity.pkl from Google Drive if not present ──
if not os.path.exists('similarity.pkl'):
    with st.spinner('Downloading model... please wait ⏳'):
        url = 'https://drive.google.com/uc?export=download&id=15CeCJv4HQrNkoqqyJoI__XIvMYtCnkv1'
        gdown.download(url, 'similarity.pkl', quiet=False, fuzzy=True)

# ── Load data ──────────────────────────────────────────────
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ── Fetch poster from TMDB ─────────────────────────────────
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ef69bfea068576224ba38e171707ca62',
            timeout=10
        )
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        else:
            return None
    except Exception:
        return None

# ── Recommend function ─────────────────────────────────────
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_posters

# ── UI ─────────────────────────────────────────────────────
st.title('🎬 Movie Mesh')
st.markdown("##### Find movies similar to what you love")
st.divider()

selected_movie_name = st.selectbox(
    'Select a movie you like',
    movies['title'].values
)

if st.button('Recommend'):
    with st.spinner('Finding matches...'):
        names, posters = recommend(selected_movie_name)

    st.subheader(f'Because you liked **{selected_movie_name}**:')
    st.write("")

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    NO_POSTER = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster if poster else NO_POSTER)
            st.caption(name)
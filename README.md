# 🎬 Movie Mesh

A content-based movie recommendation system that suggests similar movies based on your selection.

**Live Demo:** https://moviemesh.streamlit.app

---

## 🚀 Features

- Recommends 5 similar movies based on content-based filtering
- Fetches real movie posters using TMDB API
- Clean and responsive UI built with Streamlit
- Trained on TMDB 5000 Movies Dataset

---

## 🛠️ Tech Stack

- **Python** — Core programming language
- **Pandas & NumPy** — Data processing
- **Scikit-learn** — Cosine Similarity & CountVectorizer
- **NLTK** — Text stemming
- **TMDB API** — Movie poster fetching
- **Streamlit** — Frontend & deployment
- **Google Drive** — Model file hosting

---

## 📊 How It Works

1. Movie metadata (genres, cast, crew, keywords) is combined into a single **tags** column
2. **CountVectorizer** converts tags into vectors (5000 features)
3. **Cosine Similarity** measures similarity between all movie pairs
4. Top 5 most similar movies are returned as recommendations

---

## 📁 Project Structure

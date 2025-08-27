import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from recommender import Recommender 


st.set_page_config(page_title="Song Recommender", layout="wide")

st.markdown(
    """
    <style>
    .title {
        font-size:40px !important;
        font-weight:bold;
        color:#AC9362 ;
    }
    .subtitle {
        font-size:20px;
        color:gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<p class='title'>Song Recommendation System</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover songs similar to your favorites </p>", unsafe_allow_html=True)


data = pd.read_csv("songs.csv")
recommender = Recommender(data_path="songs.csv")


st.sidebar.header("Controls")
song_choice = st.sidebar.selectbox("Choose a song:", data['Title'].unique())
top_n = st.sidebar.slider("Number of Recommendations:", 3, 15, 5)


if st.sidebar.button("Recommend"):
    with st.spinner("Finding your next favorite songs..."):
        results = recommender.recommend(song_choice, top_n=top_n)

       
        st.success(f"Here are {top_n} songs similar to **{song_choice}**:")
        st.dataframe(results.style.format({"similarity": "{:.2f}"}))

        
        fig, ax = plt.subplots()
        ax.barh(results['Title'], results['similarity'], color="skyblue")
        ax.set_xlabel("Similarity Score")
        ax.set_title("Top Recommendations")
        st.pyplot(fig)

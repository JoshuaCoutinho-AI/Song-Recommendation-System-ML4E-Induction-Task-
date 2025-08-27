import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


class Recommender:
  def __init__(self, data_path = "songs.csv"):
    self.data = pd.read_csv(data_path)
    self.features = ["danceability", "energy","valence","acousticness","tempo"]
    scaler = StandardScaler()
    self.data_scaled = scaler.fit_transform(self.data[self.features])

  def recommend(self, song_title, top_n =5):
    if song_title not in self.data["Title"].values:
      return f"Song '{song_title}' not found in the dataset."
    
    indx = self.data[self.data["Title"] == song_title].index[0]

    similarity = cosine_similarity(self.data_scaled[indx].reshape(1, -1), self.data_scaled)[0]


    similar_indices = similarity.argsort()[::-1][1:top_n+1]

    recommendations = self.data.iloc[similar_indices][['Title', 'Artist']].copy()
    recommendations['similarity'] = similarity[similar_indices]
    return recommendations
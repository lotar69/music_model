import os
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

os.chdir(r'music_model')

class Data:
    def __init__(self):    
        self.X = pd.read_csv("echo_tracks.csv", index_col=0).drop(["genre_top", "track_id"], axis=1)
        self.y = pd.read_csv("echo_tracks.csv", index_col=0)["genre_top"]
        scaler = StandardScaler()
        scaled_train_X = scaler.fit_transform(self.X)
        pca = PCA(n_components=8, random_state=10)
        pca.fit(scaled_train_X)
        pca_X = pca.transform(scaled_train_X)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(pca_X, self.y, test_size=0.2)
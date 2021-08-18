____

A package for converting numerical data into a style of Music wich is Rock or Hip Hop.

This package was created by Julie & Loic for the Simplon Community.

### Features

- Convert acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo and valence for more than 2000 songs to a song type Rock or Hip Hop.

### Usage

____
import music_model

# Convert data with Decision Tree Classifier
music_model.predict.tree_prediction(acousticness= 0.416675, danceability= 0.675894, energy= 0.634476, instrumentalness= 1.062807e-02, liveness= 0.177647, speechiness= 0.159310, tempo= 165.922, valence= 0.576661) # returns Hip Hop or Rock


# Convert data with Logistic Regression
music_model.predict.log_prediction(acousticness= 0.416675, danceability= 0.675894, energy= 0.634476, instrumentalness= 1.062807e-02, liveness= 0.177647, speechiness= 0.159310, tempo= 165.922, valence= 0.576661) # returns Hip Hop or Rock
____

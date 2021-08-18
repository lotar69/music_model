from fastapi import FastAPI

from music_model.training import tree_trainer, log_trainer

import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenue sur notre application Hip Hop & Rock"}

@app.get("/tree_predict")
async def tree_prediction(acousticness= 0.416675, danceability= 0.675894, energy= 0.634476, instrumentalness= 1.062807e-02, liveness= 0.177647, speechiness= 0.159310, tempo= 165.922, valence= 0.576661):
    train_model = tree_trainer()
    data_user = {"acousticness": [acousticness],
                "danceability": [danceability],
                "energy": [energy],
                "instrumentalness": [instrumentalness],
                "liveness": [liveness],
                "speechiness": [speechiness],
                "tempo": [tempo],
                "valence": [valence]}
    data_user_df = pd.DataFrame(data_user)
    prediction = train_model.predict(data_user_df)
    return {"tree_prediction" : prediction[0]}

@app.get("/log_predict/")
async def log_prediction(acousticness= 0.416675, danceability= 0.675894, energy= 0.634476, instrumentalness= 1.062807e-02, liveness= 0.177647, speechiness= 0.159310, tempo= 165.922, valence= 0.576661):
    train_model = log_trainer()
    data_user = {"acousticness": [acousticness],
                "danceability": [danceability],
                "energy": [energy],
                "instrumentalness": [instrumentalness],
                "liveness": [liveness],
                "speechiness": [speechiness],
                "tempo": [tempo],
                "valence": [valence]}
    data_user_df = pd.DataFrame(data_user)
    prediction = train_model.predict(data_user_df)
    return {"logistic_regression": prediction[0]}

    #acousticness= 0.416675, danceability= 0.675894, energy= 0.634476, instrumentalness= 1.062807e-02, liveness= 0.177647, speechiness= 0.159310, tempo= 165.922, valence= 0.576661
    #acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence
    #0.416675, 0.675894, 0.634476, 1.062807e-02, 0.177647, 0.159310,  165.922, 0.576661

    #http://127.0.0.1:8000/tree_predict?X_test[0]
    #http://127.0.0.1:8000/log_predict?X_test[0]
# Author: ubaidrmn
# Date: March 2, 2024
# Description: A simple API for interacting with the model

from models import FeatureVector, LabelVector, CategoricalFeatures
from fastapi import FastAPI, HTTPException
from utils import *
from fastapi.middleware.cors import CORSMiddleware

import os


MODEL_PATH = os.getenv("MODEL_PATH", "../model/model.pkl")
DATASET_PATH = os.getenv("DATASET_PATH", "../model/data.csv")

DATASET = load_dataset(DATASET_PATH)
MODEL = load_model(MODEL_PATH)
SC, CT = get_original_scaler_and_encoder(DATASET)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def predict(feature: FeatureVector) -> LabelVector:
    try:
        features: FeatureVector = np.array([feature.property_type, feature.location, feature.city, feature.baths, feature.bedrooms, feature.area_marla])
        transformed_features = transform_user_input(features, SC, CT)
        prediction = MODEL.predict(transformed_features)[0]
        return {"price": prediction}
    except:
        raise HTTPException(status_code=500, detail="An error occured")


@app.get("/categorical-features")
def get_categorical_features() -> CategoricalFeatures:
    try:
        locations = {}
        for city in DATASET['city'].unique():
            locations[city] = DATASET.loc[DATASET.city == city]['location'].unique().tolist()
        cf = CategoricalFeatures(property_types=DATASET['property_type'].unique(), locations=locations, cities=DATASET['city'].unique())
        return cf
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occured")

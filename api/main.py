from typing import Union, Dict
from models import FeatureVector, LabelVector, CategoricalFeatures
from fastapi import FastAPI, HTTPException
from utils import *


DATASET = load_dataset("../model/data.csv")
MODEL = load_model("../model/model.pkl")
SC, CT = get_original_scaler_and_encoder(DATASET)
app = FastAPI()


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
        cf = CategoricalFeatures(property_types=DATASET['property_type'].unique(), locations=DATASET['location'].unique(), cities=DATASET['city'].unique())
        return cf
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occured")

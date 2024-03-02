import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib


def load_dataset(dataset_path: str):
    """
    Loads the dataset
    """
    dataset = pd.read_csv(dataset_path)
    print("[DATASET LOADED]")

    return dataset


def get_original_scaler_and_encoder(dataset):
    """
    Fits the standard scaler and one hot encoder on the original data and returns it;
    Always use this function to create SC / OHE instance as we cannot use the SC/OHE to directly 
    transform the input data from user because due to the range the output will always be 0; 
    """

    print("[INITIALIZING SCALER & ENCODER]")
    dataset = dataset.iloc[:, 1:]
    dataset = dataset.loc[(dataset.purpose == "For Sale")]
    dataset = dataset.drop('purpose', axis=1)
    X = dataset.drop('price', axis=1).values

    sc = StandardScaler()
    sc = sc.fit(X[:, 3:])
    print("[INITIALIZED SCALER]")

    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(sparse_output=False), [0, 1, 2])], remainder='passthrough')
    ct = ct.fit(X)
    print("[INITIALIZED ENCODER]")

    return sc, ct


def transform_user_input(input, sc, ct):
    """
    Transforms raw user input into usable data for the model and returns it; 
    Scales the numerical values and encodes the categorical values;
    """

    categorical_features = input[:3]
    numerical_features = input[3:].reshape(1, -1)

    scaled_numerical_features = sc.transform(numerical_features)

    processed_features = np.concatenate((categorical_features, scaled_numerical_features.flatten())).reshape(1, -1)

    processed_features = ct.transform(processed_features)
    processed_features = processed_features.astype(float)
    
    return processed_features


def load_model(model_path):
    print("[LOADING MODEL..]")
    model = joblib.load(model_path)
    print("[MODEL LOADED]")
    return model

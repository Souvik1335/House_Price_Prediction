from fastapi import APIRouter
from P2_Backend_House_Prediction.BE2_Model import model
from P2_Backend_House_Prediction.BE3_Schema import HousePricePrediction

import pandas as pd

from P1_Core_ML_House_Prediction.M1_1_Feature_Engineering import create_engineered_features


router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.post("/predict")
def predict_house_price(data: HousePricePrediction):

    # Convert API input into DataFrame
    input_data = pd.DataFrame([{
        "Area_sqft": data.Area_sqft,
        "Bedrooms": data.Bedrooms,
        "Bathrooms": data.Bathrooms,
        "Floors": data.Floors,
        "Age_of_House": data.Age_of_House,
        "Garage": data.Garage,
        "Location_Score": data.Location_Score,
        "Distance_to_City": data.Distance_to_City,
        "School_Rating": data.School_Rating,
        "Crime_Rate": data.Crime_Rate
    }])

    # Apply same feature engineering
    input_data = create_engineered_features(input_data)

    # Prediction
    prediction = model.predict(input_data)

    return {
        "predicted_price": float(prediction[0])
    }
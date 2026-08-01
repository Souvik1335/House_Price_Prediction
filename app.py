from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated
import numpy as np
import joblib

#Call FastAPI
# Create FastAPI Application
app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using a trained Random Forest Regressor model.",
    version="1.0.0"
)

#Load the dataset
model = joblib.load('house_price_model.pkl')

class HousePricePrediction(BaseModel):
    Area_sqft: Annotated[float, Field(..., gt=0, le=10000)]
    Bedrooms: Annotated[int, Field(..., ge=1, le=7)]
    Bathrooms: Annotated[int, Field(..., ge=1, le=3)]
    Floors: Annotated[int, Field(..., ge=1, le=3)]
    Age_of_House: Annotated[float, Field(..., ge=0, le=50)]
    Garage: Annotated[int, Field(..., ge=0, le=1)]
    Location_Score: Annotated[float, Field(..., ge=0, le=10)]
    Distance_to_City: Annotated[float, Field(..., ge=0)]
    School_Rating: Annotated[int, Field(..., ge=1, le=10)]
    Crime_Rate: Annotated[float, Field(..., ge=0, le=10)]

@app.get('/')
def First_Comment():
    return {'Message' : 'House Price Prediction Model API'}

@app.get('/about')
def About():
    return {'Message' : 'It is a House Prediction Model'}

# Prediction Endpoint
@app.post("/predict")
def predict(data: HousePricePrediction):
    """
    Predict the price of a house.
    """

    try:
        input_features = np.array([[
            data.Area_sqft,
            data.Bedrooms,
            data.Bathrooms,
            data.Floors,
            data.Age_of_House,
            data.Garage,
            data.Location_Score,
            data.Distance_to_City,
            data.School_Rating,
            data.Crime_Rate
        ]])

        prediction = model.predict(input_features)[0]

        return {
            "status": "success",
            "predicted_price": round(float(prediction), 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

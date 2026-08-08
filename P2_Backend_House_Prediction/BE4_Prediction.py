from fastapi import APIRouter
from P2_Backend_House_Prediction.BE2_Model import model
from P2_Backend_House_Prediction.BE3_Schema import HousePricePrediction
from fastapi import Depends
from P2_Backend_House_Prediction.BE10_JWT_Verification import get_current_user
import pandas as pd
from P2_Backend_House_Prediction.M1_1_Feature_Engineering import create_engineered_features
from P2_Backend_House_Prediction.BE6_Database_Model import (User, PredictionHistory)
from P2_Backend_House_Prediction.BE5_User_Database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.post("/predict")
def predict_house_price(data: HousePricePrediction, 
                        current_user: User = Depends(get_current_user), 
                        db: Session = Depends(get_db)):

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


    new_history = PredictionHistory(
    user_id=current_user.id,
    area_sqft=data.Area_sqft,
    bedrooms=data.Bedrooms,
    bathrooms=data.Bathrooms,
    predicted_price=float(prediction[0]))

    db.add(new_history)
    db.commit()
    db.refresh(new_history)

    return {
        "user_id": current_user.id,
        "user_name": current_user.name,
        "predicted_price": float(prediction[0])
    }
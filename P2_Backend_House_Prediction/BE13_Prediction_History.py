from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from P2_Backend_House_Prediction.BE5_User_Database import get_db
from P2_Backend_House_Prediction.BE6_Database_Model import PredictionHistory, User
from P2_Backend_House_Prediction.BE10_JWT_Verification import get_current_user


router = APIRouter(
    prefix="/prediction",
    tags=["Prediction History"]
)


@router.get("/history")
def get_prediction_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    history = db.query(PredictionHistory).filter(
        PredictionHistory.user_id == current_user.id
    ).all()

    return [
        {
            "Date": prediction.created_at.strftime("%d %b %Y"),
            "Area (sqft)": prediction.area_sqft,
            "Bedrooms": prediction.bedrooms,
            "Bathrooms": prediction.bathrooms,
            "Predicted Price (₹)": f"₹ {prediction.predicted_price:,.0f}"
        }

        for prediction in history
    ]
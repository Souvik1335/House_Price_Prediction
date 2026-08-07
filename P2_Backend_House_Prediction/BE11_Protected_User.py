from fastapi import APIRouter, Depends

from P2_Backend_House_Prediction.BE6_Database_Model import User
from P2_Backend_House_Prediction.BE10_JWT_Verification import get_current_user


router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.get("/me")
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "message": "Authentication successful",
        "user_id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
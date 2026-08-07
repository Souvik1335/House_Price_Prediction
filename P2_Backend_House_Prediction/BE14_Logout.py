from fastapi import APIRouter, Depends
from P2_Backend_House_Prediction.BE10_JWT_Verification import get_current_user
from P2_Backend_House_Prediction.BE6_Database_Model import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/logout")
def logout(
    current_user: User = Depends(get_current_user)
):

    return {
        "message": "Logout successful",
        "user_id": current_user.id,
        "email": current_user.email
    }
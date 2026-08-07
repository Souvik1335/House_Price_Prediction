from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from P2_Backend_House_Prediction.BE5_User_Database import get_db
from P2_Backend_House_Prediction.BE6_Database_Model import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Forgot Password Schema

class ForgotPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str
    confirm_password: str



# Forgot Password API

@router.post("/forgot-password")
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):

    # Find user by email
    user = db.query(User).filter(
        User.email == data.email
    ).first()


    if not user:
        raise HTTPException(
            status_code=404,
            detail="Email not registered"
        )


    # Check password confirmation

    if data.new_password != data.confirm_password:
        raise HTTPException(
            status_code=400,
            detail="Passwords do not match"
        )


    # Hash new password

    new_hashed_password = pwd_context.hash(
        data.new_password
    )


    # Update password

    user.password_hash = new_hashed_password


    db.commit()
    db.refresh(user)


    return {
        "message": "Password reset successful",
        "email": user.email
    }
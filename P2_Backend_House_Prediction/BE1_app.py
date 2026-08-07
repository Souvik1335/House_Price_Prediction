from fastapi import FastAPI, Depends, HTTPException
from P2_Backend_House_Prediction.BE2_Model import model
from P2_Backend_House_Prediction.BE4_Prediction import router as prediction_router
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from P2_Backend_House_Prediction.BE3_Schema import UserRegistration
from P2_Backend_House_Prediction.BE5_User_Database import get_db
from P2_Backend_House_Prediction.BE6_Database_Model import User
from P2_Backend_House_Prediction.BE8_Login import router as login_router
from P2_Backend_House_Prediction.BE11_Protected_User import router as user_router
from P2_Backend_House_Prediction.BE12_Forgot_Reset_Password import router as forgot_password_router
from P2_Backend_House_Prediction.BE13_Prediction_History import router as history_router
from P2_Backend_House_Prediction.BE14_Logout import router as logout_router


# For PAssword Hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices using a trained machine learning model.",
    version="1.0.0"
)

# For User Logout 
app.include_router(logout_router)

# For Prediction History
app.include_router(history_router)

# For Forgot Password
app.include_router(forgot_password_router)

# For User Router
app.include_router(user_router)

# For Login Router
app.include_router(login_router)

@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }

# User Registration
@app.post("/register")
def register_user(
    data: UserRegistration,
    db: Session = Depends(get_db)
):

    # Check if email already exists
    existing_email = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Check if personal phone already exists
    existing_phone = db.query(User).filter(
        User.personal_phone == data.personal_phone
    ).first()

    if existing_phone:
        raise HTTPException(
            status_code=400,
            detail="Personal phone number already registered"
        )

    # Hash password
    hashed_password = pwd_context.hash(data.password)

    # Create user
    new_user = User(
        name=data.name,
        email=str(data.email),
        personal_phone=data.personal_phone,
        alternate_phone=data.alternate_phone,
        password_hash=hashed_password,
        date_of_birth=data.date_of_birth
    )

    # Save user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Registration successful",
        "user_id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }





app.include_router(prediction_router)


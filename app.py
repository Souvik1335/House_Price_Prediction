from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated
import numpy as np
import joblib
import sqlite3
import warnings
import bcrypt
from sklearn.exceptions import InconsistentVersionWarning
import random
from datetime import datetime, timedelta
from email_Service import send_otp_email
from auth import create_access_token, get_current_user,create_refresh_token
from fastapi.security import OAuth2PasswordRequestForm

warnings.filterwarnings(
    "ignore",
    category=InconsistentVersionWarning
)

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
    Bedrooms: Annotated[int, Field(..., ge=1, le=10)]
    Bathrooms: Annotated[int, Field(..., ge=1, le=10)]
    Floors: Annotated[int, Field(..., ge=1, le=3)]
    Age_of_House: Annotated[float, Field(..., ge=0, le=50)]
    Garage: Annotated[int, Field(..., ge=0, le=1)]
    Location_Score: Annotated[float, Field(..., ge=0, le=10)]
    Distance_to_City: Annotated[float, Field(..., ge=0)]
    School_Rating: Annotated[int, Field(..., ge=1, le=10)]
    Crime_Rate: Annotated[float, Field(..., ge=0, le=10)]

class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    date_of_birth: str
    alternate_phone_number: str
    payment_type: str
    emi_years: int
    interest_rate: float

@app.get('/')
def home():
    return {'Message' : 'House Price Prediction Model API'}

@app.get('/about')
def about():
    return {'Message' : 'It is a House Prediction Model'}

    
@app.post("/register")
async def register(user: RegisterUser):

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    password_bytes = user.password.encode('utf-8')

    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    hashed_password = hashed_password.decode("utf-8")

    try:
        otp = str(random.randint(100000, 999999))

        otp_expiry = (
            datetime.now() + timedelta(minutes=5)
            ).strftime("%Y-%m-%d %H:%M:%S")
        
        # Check if email already exists
        cursor.execute(
            "SELECT id FROM User_Database WHERE email = ?",
            (user.email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered."
            )
        
        cursor.execute("""
        INSERT INTO User_Database(
        name,
        email,
        phone,
        password,
        Date_of_Birth,
        alternate_phone_number,
        payment_type,
        emi_years,
        interest_rate,
        otp,
        otp_expiry
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            user.name,
            user.email,
            user.phone,
            hashed_password,
            user.date_of_birth,
            user.alternate_phone_number,
            user.payment_type,
            user.emi_years,
            user.interest_rate,
            otp,
            otp_expiry

        ))

        connection.commit()

        # await send_otp_email(user.email, otp)

        return {
            "Message": "User Registered Successfully"
        }

    finally:
        connection.close()

class VerifyEmail(BaseModel):
    email: EmailStr
    otp: str

@app.post("/verify-email")
def verify_email(user: VerifyEmail):

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT otp, otp_expiry
            FROM User_Database
            WHERE email = ?
        """, (user.email,))

        result = cursor.fetchone()

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Email not found."
            )

        stored_otp = result[0]
        otp_expiry = result[1]

        if stored_otp != user.otp:
            raise HTTPException(
                status_code=400,
                detail="Invalid OTP."
            )

        expiry_time = datetime.strptime(
            otp_expiry,
            "%Y-%m-%d %H:%M:%S"
        )

        if datetime.now() > expiry_time:
            raise HTTPException(
                status_code=400,
                detail="OTP Expired."
            )

        cursor.execute("""
            UPDATE User_Database
            SET email_verified = 1,
                otp = NULL,
                otp_expiry = NULL
            WHERE email = ?
        """, (user.email,))

        connection.commit()

        return {
            "message": "Email verified successfully."
        }

    finally:
        connection.close()

class UserLogin(BaseModel):
    email : EmailStr
    password : str

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    email = form_data.username.strip()

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    try:

        # Check whether email exists
        cursor.execute("""
            SELECT password
            FROM User_Database
            WHERE email = ?
        """, (email,))

        result = cursor.fetchone()

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Email Not Found"
            )

        stored_password = result[0]

        # Verify password
        if not bcrypt.checkpw(
            form_data.password.encode("utf-8"),
            stored_password.encode("utf-8")
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid Password"
            )

        # Generate Access Token
        access_token = create_access_token(
            data={
                "sub": email
            }
        )

        # Generate Refresh Token
        refresh_token = create_refresh_token(
            data={
                "sub": email
            }
        )

        # Return both tokens
        return {
            "message": "Login Successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    finally:
        connection.close()

class ForgotPassword(BaseModel):
    email: EmailStr

@app.post("/forgot-password")
async def forgot_password(user: ForgotPassword):

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    try:

        # Check whether email exists
        cursor.execute("""
            SELECT id
            FROM User_Database
            WHERE email = ?
        """, (user.email,))

        existing_user = cursor.fetchone()

        if existing_user is None:
            raise HTTPException(
                status_code=404,
                detail="Email Not Found"
            )

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        otp_expiry = (
            datetime.now() + timedelta(minutes=5)
        ).strftime("%Y-%m-%d %H:%M:%S")

        # Save OTP
        cursor.execute("""
            UPDATE User_Database
            SET otp = ?,
                otp_expiry = ?
            WHERE email = ?
        """, (
            otp,
            otp_expiry,
            user.email
        ))

        connection.commit()

        # Send OTP
        await send_otp_email(user.email, otp)

        return {
            "message": "OTP sent successfully to your email."
        }

    finally:
        connection.close()

class ResetPassword(BaseModel):
    email: EmailStr
    otp: str
    new_password: str

@app.post("/reset-password")
async def reset_password(user: ResetPassword):

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    try:

        # Check email, OTP and expiry
        cursor.execute("""
            SELECT otp, otp_expiry
            FROM User_Database
            WHERE email = ?
        """, (user.email,))

        result = cursor.fetchone()

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Email Not Found"
            )

        stored_otp = result[0]
        otp_expiry = result[1]

        # Verify OTP
        if stored_otp != user.otp:
            raise HTTPException(
                status_code=400,
                detail="Invalid OTP"
            )

        # Check OTP expiry
        expiry_time = datetime.strptime(
            otp_expiry,
            "%Y-%m-%d %H:%M:%S"
        )

        if datetime.now() > expiry_time:
            raise HTTPException(
                status_code=400,
                detail="OTP Expired"
            )

        # Hash new password
        hashed_password = bcrypt.hashpw(
            user.new_password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # Update password and clear OTP
        cursor.execute("""
            UPDATE User_Database
            SET password = ?,
                otp = NULL,
                otp_expiry = NULL
            WHERE email = ?
        """, (
            hashed_password,
            user.email
        ))

        connection.commit()

        return {
            "message": "Password reset successful."
        }

    finally:
        connection.close()

def get_user_profile(email: str):

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            email,
            phone,
            Date_of_Birth,
            alternate_phone_number,
            payment_type,
            emi_years,
            interest_rate
        FROM User_Database
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    connection.close()

    return user


@app.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {
        "email": current_user
    }

@app.get("/profile")
def profile(current_user: str = Depends(get_current_user)):

    user = get_user_profile(current_user)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user[0],
        "name": user[1],
        "email": user[2],
        "phone": user[3],
        "date_of_birth": user[4],
        "alternate_phone_number": user[5],
        "payment_type": user[6],
        "emi_years": user[7],
        "interest_rate": user[8]
    }

@app.post("/predict")
def predict(
    data: HousePricePrediction,
    current_user: str = Depends(get_current_user)
):

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

        connection = sqlite3.connect("User_Database.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO Prediction_History(

            user_email,
            Area_sqft,
            Bedrooms,
            Bathrooms,
            Floors,
            Age_of_House,
            Garage,
            Location_Score,
            Distance_to_City,
            School_Rating,
            Crime_Rate,
            Predicted_Price,
            Prediction_Time

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            current_user,
            data.Area_sqft,
            data.Bedrooms,
            data.Bathrooms,
            data.Floors,
            data.Age_of_House,
            data.Garage,
            data.Location_Score,
            data.Distance_to_City,
            data.School_Rating,
            data.Crime_Rate,
            float(prediction),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ))

        connection.commit()
        connection.close()

        return {
            "status": "success",
            "predicted_price": round(float(prediction), 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/prediction-history")
def get_prediction_history(
    current_user: str = Depends(get_current_user)
):

    try:

        connection = sqlite3.connect("User_Database.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT
            Area_sqft,
            Bedrooms,
            Bathrooms,
            Floors,
            Age_of_House,
            Predicted_Price,
            Prediction_Time

        FROM Prediction_History

        WHERE user_email = ?

        ORDER BY Prediction_Time DESC

        """, (current_user,))


        history = cursor.fetchall()

        connection.close()


        return {
            "history": history
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    
@app.get("/users")
def users():

    connection = sqlite3.connect("User_Database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, email FROM User_Database")

    data = cursor.fetchall()

    connection.close()

    return data

@app.post("/logout")
def logout(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": f"{current_user} logged out successfully"
    }
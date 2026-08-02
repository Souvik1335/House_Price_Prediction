from fastapi import FastAPI, HTTPException
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
    Bedrooms: Annotated[int, Field(..., ge=1, le=7)]
    Bathrooms: Annotated[int, Field(..., ge=1, le=3)]
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

        await send_otp_email(user.email, otp)

        return {
            "Message": "User Registered Successfully"
        }

    finally:
        connection.close()

class UserLogin(BaseModel):
    email : EmailStr
    password : str

@app.post('/login')
def login(user:UserLogin):
    connection = sqlite3.connect('User_Database.db')
    cursor = connection.cursor()

    try:
        
        cursor.execute("""
        SELECT password FROM User_Database WHERE email = ?
        """, (user.email,))

        result = cursor.fetchone()

        if result is None:
            raise HTTPException(status_code=404, detail='Email Not Found')

        stored_password = result[0]

        if bcrypt.checkpw(
            user.password.encode("utf-8"),
            stored_password.encode("utf-8")):

                return {
                    'Message' : 'User Login Successful'
                    }
        else:
            raise HTTPException(status_code=401, detail='Invalid Password')

    finally:
        connection.close()



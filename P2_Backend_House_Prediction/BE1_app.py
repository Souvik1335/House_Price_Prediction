from fastapi import FastAPI
from P2_Backend_House_Prediction.BE2_Model import model
from P2_Backend_House_Prediction.BE4_Prediction import router as prediction_router

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices using a trained machine learning model.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }

app.include_router(prediction_router)
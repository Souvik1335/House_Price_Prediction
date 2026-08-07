import joblib
from M3_Model_Training import model

joblib.dump(model, "house_price_model.pkl")

print("Model saved successfully!")
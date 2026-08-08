from pathlib import Path
import sys
import joblib

PROJECT_ROOT = Path(__file__).resolve().parent

# Path to the trained ML model
MODEL_PATH = PROJECT_ROOT / "house_price_model.pkl"

# Load the trained model
model = joblib.load(MODEL_PATH)

print("ML model loaded successfully.")
print("Expected number of features:", model.n_features_in_)
print("Expected feature names:", model.feature_names_in_)
from pathlib import Path
import sys
import joblib


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Get the project root directory
BASE_DIR = PROJECT_ROOT

# Path to the trained ML model
MODEL_PATH = BASE_DIR / "P1_Core_ML_House_Prediction" / "house_price_model.pkl"

# Load the trained model
model = joblib.load(MODEL_PATH)

print("ML model loaded successfully.")
print("Expected number of features:", model.n_features_in_)
print("Expected feature names:", model.feature_names_in_)
import requests

from config import BASE_URL


# -----------------------------
# Register User
# -----------------------------
def register_user(user_data):

    try:

        response = requests.post(
            f"{BASE_URL}/register",
            json=user_data
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Verify Email (Registration)
# -----------------------------
def verify_email(data):

    try:

        response = requests.post(
            f"{BASE_URL}/verify-email",
            json=data
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Login
# -----------------------------
def login_user(email, password):

    try:

        response = requests.post(
            f"{BASE_URL}/login",
            data={
                "username": email,
                "password": password
            }
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Get User Profile
# -----------------------------
def get_profile(access_token):

    try:

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(
            f"{BASE_URL}/profile",
            headers=headers
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Predict House Price
# -----------------------------
def predict_house_price(data, access_token):

    try:

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.post(
            f"{BASE_URL}/predict",
            json=data,
            headers=headers
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Prediction History
# -----------------------------
def get_prediction_history(access_token):

    try:

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(
            f"{BASE_URL}/prediction-history",
            headers=headers
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Forgot Password
# -----------------------------
def forgot_password(email):

    try:

        response = requests.post(
            f"{BASE_URL}/forgot-password",
            json={
                "email": email
            }
        )

        return response

    except Exception as e:

        return e


# -----------------------------
# Reset Password
# -----------------------------
def reset_password(data):

    try:

        response = requests.post(
            f"{BASE_URL}/reset-password",
            json=data
        )

        return response

    except Exception as e:

        return e
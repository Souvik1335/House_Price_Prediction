import requests

from utils.config import BASE_URL

# Call the API for Register new User
def register_user(user_data: dict):

    url = f"{BASE_URL}/register"

    response = requests.post(
        url=url,
        json=user_data
    )

    return response

# Call the API for getting Login
def login_user(email: str, password: str):

    url = f"{BASE_URL}/auth/login"

    response = requests.post(
        url=url,
        data={
            "username": email,   # OAuth2 expects "username"
            "password": password
        }
    )

    return response

# Call the API for getting House Price Prediction
def get_prediction(token: str, house_data: dict):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        url=f"{BASE_URL}/prediction/predict",
        headers=headers,
        json=house_data
    )

    return response 

# Call the API for getting Reset Password
def reset_password(email: str, new_password: str, confirm_password: str):

    url = f"{BASE_URL}/auth/forgot-password"

    response = requests.post(
        url=url,
        json={
            "email": email,
            "new_password": new_password,
            "confirm_password": confirm_password
        }
    )

    return response

# Call the API for getting User Profile
def get_profile(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/user/me",
        headers=headers
    )

    return response

#Call the API for grtting Previous House Prediction History
def get_prediction_history(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        url=f"{BASE_URL}/prediction/history",
        headers=headers
    )

    return response

# Call the API for getting Logout
def logout_user(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        url=f"{BASE_URL}/auth/logout",
        headers=headers
    )

    return response
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

#Secrect Key
Secret_Key = "Your Super Secret Key is here Change this"
Algorithm = "HS256"
Access_Token_Expire_Time = 30
Refresh_Token_Expire_Time = 7

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=Access_Token_Expire_Time)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
    to_encode,
    Secret_Key,
    algorithm=Algorithm
)
    return encoded_jwt

def create_refresh_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        days=Refresh_Token_Expire_Time
    )

    to_encode.update({"exp": expire})

    refresh_token = jwt.encode(
        to_encode,
        Secret_Key,
        algorithm=Algorithm
    )

    return refresh_token

def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            Secret_Key,
            algorithms=[Algorithm]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or Expired Token"
        )

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_access_token(token)

    email = payload.get("sub")

    if email is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    return email
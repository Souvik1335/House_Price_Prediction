from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("EMAIL"),
    MAIL_PASSWORD=os.getenv("EMAIL_PASSWORD"),
    MAIL_FROM=os.getenv("EMAIL"),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

async def send_otp_email(receiver_email: str, otp: str):

    message = MessageSchema(
        subject="House Price Prediction - Email Verification",
        recipients=[receiver_email],
        body=f"""
        <h2>Email Verification</h2>

        <p>Your OTP is:</p>

        <h1>{otp}</h1>

        <p>This OTP is valid for 5 minutes.</p>

        <br>

        <p>Do not share this OTP with anyone.</p>
        """,
        subtype=MessageType.html
    )

    fm = FastMail(conf)

    await fm.send_message(message)
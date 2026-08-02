from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from dotenv import load_dotenv
import os

load_dotenv()

print("EMAIL =", os.getenv("EMAIL"))
print("PASSWORD =", os.getenv("EMAIL_PASSWORD"))


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

    print("=" * 50)
    print("Receiver:", receiver_email)
    print("OTP:", otp)

    message = MessageSchema(
        subject="House Price Prediction - Email Verification",
        recipients=[receiver_email],
        body=f"""
        <h2>Email Verification</h2>
        <h1>{otp}</h1>
        """,
        subtype=MessageType.html
    )

    fm = FastMail(conf)

    print("Before send_message()")
    await fm.send_message(message)
    print("After send_message()")
    print("=" * 50)
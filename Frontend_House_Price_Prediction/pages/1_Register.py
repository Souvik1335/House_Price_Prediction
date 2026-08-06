import re
from datetime import date
import streamlit as st
from validators import (
    validate_email,
    validate_phone,
    validate_password
)
from api import register_user
 
# Page Configuration
st.set_page_config(
    page_title="User Registration",
    page_icon="📝",
    layout="centered"
)
 
st.title("📝 Create Your Account")
st.caption("Please fill in the details below.")
 
BASE_INTEREST_RATE = 8.0
INTEREST_INCREMENT = 0.20
 
 
# User's Personal Information
st.subheader("👤 Personal Information")
 
name = st.text_input("Full Name")
 
email = st.text_input("Email Address")
 
phone = st.text_input("Phone Number")
 
alternate_phone = st.text_input("Alternate Phone Number")
 
date_of_birth = st.date_input(
    "Date of Birth",
    min_value=date(1950, 1, 1),
    max_value=date.today()
)
 
st.divider()
 
 
# Account Security
st.subheader("🔐 Account Security")
 
show_password = st.checkbox("Show Password")
 
password = st.text_input(
    "Password",
    type="default" if show_password else "password"
)
 
confirm_password = st.text_input(
    "Confirm Password",
    type="default" if show_password else "password"
)
 
st.info("""
Password must contain:
 
• Minimum 8 characters
 
• One uppercase letter
 
• One lowercase letter
 
• One number
 
• One special character
""")
 
st.divider()
 
 
# Payment Method
st.subheader("💳 Payment Information")
 
payment_type = st.radio(
    "Select Payment Type",
    [
        "Cash",
        "EMI"
    ]
)
 
emi_years = 0
interest_rate = 0.0
 
if payment_type == "EMI":
 
    emi_years = st.slider(
        "EMI Years",
        min_value=1,
        max_value=10,
        value=1
    )
 
    interest_rate = BASE_INTEREST_RATE + \
        (emi_years - 1) * INTEREST_INCREMENT
 
    st.success(
        f"Interest Rate : {interest_rate:.2f}%"
    )
 
st.divider()
 
 
# Validation Status (shown together at the bottom, instead of under each field)
st.subheader("📋 Validation Status")
 
if email:
    if validate_email(email):
        st.success("Valid Email Address")
    else:
        st.error("Invalid Email Address")
 
if phone:
    if validate_phone(phone):
        st.success("Valid Phone Number")
    else:
        st.error("Invalid Phone Number")
 
if alternate_phone:
    if validate_phone(alternate_phone):
        st.success("Valid Alternate Phone Number")
    else:
        st.error("Invalid Alternate Phone Number")
 
st.divider()
 
 
# Registration Complete & Registered User's Information
if st.button("🚀 Register", use_container_width=True):
 
    if not name.strip():
        st.error("❌ Full Name is required.")
 
    elif not email.strip():
        st.error("❌ Email Address is required.")
 
    elif not phone.strip():
        st.error("❌ Phone Number is required.")
 
    elif not alternate_phone.strip():
        st.error("❌ Alternate Phone Number is required.")
 
    elif not password:
        st.error("❌ Password is required.")
 
    elif not confirm_password:
        st.error("❌ Confirm Password is required.")
 
    elif not validate_email(email):
        st.error("❌ Please enter a valid Email Address.")
 
    elif not validate_phone(phone):
        st.error("❌ Please enter a valid 10-digit Phone Number.")
 
    elif not validate_phone(alternate_phone):
        st.error("❌ Please enter a valid 10-digit Alternate Phone Number.")
 
    elif phone == alternate_phone:
        st.error("❌ Phone Number and Alternate Phone Number cannot be the same.")
 
    else:
 
        valid_password, message = validate_password(password)
 
        if not valid_password:
            st.error(message)
 
        elif password != confirm_password:
            st.error("❌ Passwords do not match.")
 
        else:
 
            with st.spinner("Creating your account..."):

                user_data = {

                    "name": name,
                    "email": email,
                    "phone": phone,
                    "date_of_birth": str(date_of_birth),
                    "alternate_phone_number": alternate_phone,
                    "payment_type": payment_type,
                    "emi_years": emi_years,
                    "interest_rate": interest_rate,
                    "password": password

                }


                response = register_user(user_data)


                if response.status_code == 200:

                    st.success(
                        "✅ Registration Successful! OTP sent to your email."
                    )


                    st.session_state["email"] = email


                    st.switch_page(
                        "pages/2_Email_Verification.py"
                    )


                else:

                    st.error(
                        response.json()
                    )
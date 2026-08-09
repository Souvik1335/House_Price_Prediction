import streamlit as st
from datetime import date
from utils.api import register_user


# Page Configuration
st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)


# Title
st.title("📝 Create Your Account")

st.write(
    "Please fill in the details below to register."
)


st.divider()
# Registration Form
with st.form("registration_form"):

    name = st.text_input(
        "👤 Full Name",
        placeholder="Enter your full name"
    )

    email = st.text_input(
        "📧 Email Address",
        placeholder="example@gmail.com"
    )

    personal_phone = st.text_input(
        "📱 Personal Phone Number",
        placeholder="10-digit mobile number"
    )

    alternate_phone = st.text_input(
        "☎️ Alternate Phone Number (Optional)",
        placeholder="Optional"
    )

    dob = st.date_input(
        "🎂 Date of Birth",
        min_value=date(1950, 1, 1),
        max_value=date.today()
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password",
        placeholder="Confirm password"
    )

    submitted = st.form_submit_button(
        "📝 Register",
        use_container_width=True
    )


# Validation
if submitted:

    if not name.strip():
        st.error("Full Name is required.")

    elif not email.strip():
        st.error("Email is required.")

    elif not personal_phone.strip():
        st.error("Personal Phone Number is required.")

    elif len(personal_phone) != 10 or not personal_phone.isdigit():
        st.error("Enter a valid 10-digit Personal Phone Number.")

    elif alternate_phone and (
        len(alternate_phone) != 10 or not alternate_phone.isdigit()
    ):
        st.error("Enter a valid 10-digit Alternate Phone Number.")

    elif not password:
        st.error("Password is required.")

    elif len(password) < 8:
        st.error("Password must contain at least 8 characters.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        with st.spinner("Creating your account..."):

            user_data = {
                "name": name,
                "email": email,
                "personal_phone": personal_phone,
                "alternate_phone": alternate_phone,
                "password": password,
                "confirm_password": confirm_password,
                "date_of_birth": str(dob)
            }

            response = register_user(user_data)

            if response.status_code == 200:

                st.success("✅ Registration Successful!")

                st.info("You can now login to your account.")

            else:
                st.write("STATUS:", response.status_code)
                st.write("RESPONSE:", response.text)

st.divider()

st.write("Already have an account?")

if st.button(
    "🔐 Login",
    use_container_width=True
):
    st.switch_page("pages/FE3_Login.py")
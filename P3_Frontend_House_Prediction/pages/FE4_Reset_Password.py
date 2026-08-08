import streamlit as st
from utils.api import reset_password

# Page Configuration
st.set_page_config(
    page_title="Reset Password",
    page_icon="🔑",
    layout="centered")


# Title
st.title("🔑 Reset Password")

st.write("Create a new password for your account.")

st.divider()

# Reset Password Form
with st.form("reset_password_form"):
    email = st.text_input(
    "📧 Email Address",
    placeholder="example@gmail.com"
)

    new_password = st.text_input(
        "🔒 New Password",
        type="password",
        placeholder="Enter your new password")

    confirm_password = st.text_input(
        "🔒 Confirm New Password",
        type="password",
        placeholder="Confirm your new password")

    submitted = st.form_submit_button(
        "🔄 Reset Password",
        use_container_width=True)


# Validation
if submitted:
    if not new_password:
        st.error("New Password is required.")
    elif len(new_password) < 8:
        st.error("Password must contain at least 8 characters.")
    elif new_password != confirm_password:
        st.error("Passwords do not match.")
    else:
        with st.spinner("Resetting password..."):
            response = reset_password(
            email=email,
            new_password=new_password,
            confirm_password=confirm_password
        )

        if response.status_code == 200:
            st.success("✅ Password Reset Successful!")
            st.info("Please login with your new password.")

        else:
            st.error(response.json()["detail"])

st.divider()
# Back to Login Button
if st.button(
    "⬅ Back to Login",
    use_container_width=True
):
    st.switch_page("pages/FE3_Login.py")
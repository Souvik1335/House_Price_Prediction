import streamlit as st
from utils.api import get_profile, logout_user
import requests

# Page Configuration
st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered")


# Login Check
if "token" not in st.session_state:
    st.session_state.token = None

if st.session_state.token is None:
    st.warning("Please login first.")
    st.switch_page("pages/FE3_Login.py")


# Title
st.title("👤 My Profile")
st.write("View your account information.")

st.divider()

# Temporary User Data

# st.write(st.session_state.token)
response = get_profile(st.session_state.token)

if response.status_code == 200:
    user = response.json()
else:
    st.error("Unable to load profile.")
    st.stop()

# Profile Information
st.subheader("Personal Information")

st.text_input(
    "👤 Full Name",
    value=user["name"],
    disabled=True
)

st.text_input(
    "📧 Email",
    value=user["email"],
    disabled=True
)

st.text_input(
    "📱 Personal Phone",
    value=user["personal_phone"],
    disabled=True
)

st.text_input(
    "☎️ Alternate Phone",
    value=user["alternate_phone"],
    disabled=True
)

st.text_input(
    "🎂 Date of Birth",
    value=user["date_of_birth"],
    disabled=True
)

st.text_input(
    "📅 Account Created",
    value=user["created_at"],
    disabled=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🏠 Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/FE5_Dashboard.py")

with col2:
    if st.button(
    "🚪 Logout",
    use_container_width=True
):
        with st.spinner("Logging out..."):

            response = logout_user(
                st.session_state.token
            )

            if response.status_code == 200:
                st.session_state.token = None
                st.success("✅ Logged out successfully!")
                st.switch_page("FE1_Frontend_app.py")

            else:
                try:
                    detail = response.json().get(
                        "detail",
                        "Unable to logout."
                    )
                    st.error(detail)

                except requests.exceptions.JSONDecodeError:
                    st.error(
                        f"Backend Error: {response.status_code}"
                    )
                    st.code(response.text)
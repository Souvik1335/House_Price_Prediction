import streamlit as st
from utils.api import login_user


# Page Configuration
st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)


# Session State
if "token" not in st.session_state:
    st.session_state.token = None

# Title
st.title("🔐 Login")

st.write(
    "Welcome back! Please login to continue."
)

st.divider()


# Login Form
with st.form("login_form"):

    email = st.text_input(
        "📧 Email Address",
        placeholder="example@gmail.com"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter your password"
    )

    submitted = st.form_submit_button(
        "🔐 Login",
        use_container_width=True
    )


# Validation
if submitted:

    if not email.strip():
        st.error("Email is required.")

    elif not password:
        st.error("Password is required.")

    else:

        with st.spinner("Logging in..."):

            # Backend API will be added later
            response = login_user(email, password)

            if response.status_code == 200:
                token = response.json()["access_token"]
                st.session_state.token = token
                st.success("✅ Login Successful!")
                st.switch_page("pages/FE5_Dashboard.py")
            else:
                st.error(response.json()["detail"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🔑 Forgot Password",
        use_container_width=True
    ):
        st.switch_page("pages/FE4_Reset_Password.py")

with col2:
    if st.button(
        "📝 Register",
        use_container_width=True
    ):
        st.switch_page("pages/FE2_Register.py")
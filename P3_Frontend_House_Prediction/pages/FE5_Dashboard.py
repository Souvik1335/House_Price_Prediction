import streamlit as st
from utils.api import logout_user


# Page Configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon="🏠",
    layout="wide")


# Login Check
if "token" not in st.session_state:
    st.session_state.token = None

if st.session_state.token is None:
    st.warning("Please login first.")
    st.switch_page("pages/FE3_Login.py")


# Title
st.title("🏠 Dashboard")
st.write("Welcome to the House Price Prediction System.")

st.divider()

# Navigation Cards
col1, col2 = st.columns(2)
with col1:
    st.subheader("👤 Profile")
    st.write("View your personal information.")

    if st.button(
        "Open Profile",
        use_container_width=True):
        st.switch_page("pages/FE6_Profile.py")

with col2:
    st.subheader("🏠 House Price Prediction")
    st.write("Predict the market price of a house.")

    if st.button(
        "Predict House Price",
        use_container_width=True):
        st.switch_page("pages/FE7_House_Prediction.py")

st.divider()

col3, col4 = st.columns(2)
with col3:
    st.subheader("📜 Prediction History")
    st.write("View all previous predictions.")

    if st.button(
        "Prediction History",
        use_container_width=True):
        st.switch_page("pages/FE8_Prediction_History.py")

with col4:
    st.subheader("🚪 Logout")
    st.write("Logout from your account.")

    if st.button(
        "Logout",
        use_container_width=True):
        with st.spinner("Logging out..."):

            response = logout_user(
                st.session_state.token
            )

            if response.status_code == 200:

                st.session_state.token = None

                st.success("✅ Logged out successfully!")

                st.switch_page("FE1_Frontend_app.py")

            else:

                st.error(response.json()["detail"])
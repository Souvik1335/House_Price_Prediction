import streamlit as st


# Page Configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# Session State
if "token" not in st.session_state:
    st.session_state.token = None


# Title
st.title("🏠 House Price Prediction System")

st.markdown(
"""
### Welcome!

Welcome to the **House Price Prediction System**.

This application uses **Machine Learning** to estimate house prices based on user-provided property details.

### ✨ Features

- 👤 Secure User Registration
- 🔐 Login Authentication
- 🏠 House Price Prediction
- 📜 Prediction History
- 👤 User Profile

---
"""
)


# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/FE3_Login.py")

with col2:
    if st.button("📝 Register", use_container_width=True):
        st.switch_page("pages/FE2_Register.py")


st.divider()

# Footer
st.caption("Built with ❤️ using FastAPI • Streamlit • Machine Learning")
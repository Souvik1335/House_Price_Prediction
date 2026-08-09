import streamlit as st
import pandas as pd
from utils.api import get_prediction_history
import requests

# Page Configuration
st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)


# Login Check
if "token" not in st.session_state:
    st.session_state.token = None

if st.session_state.token is None:
    st.warning("Please login first.")
    st.switch_page("pages/FE3_Login.py")


# Title
st.title("📜 Prediction History")
st.write("View all your previous house price predictions.")

st.divider()

response = get_prediction_history(
    st.session_state.token
)

if response.status_code == 200:

    history = pd.DataFrame(
        response.json()
    )

else:

    try:
        detail = response.json().get(
            "detail",
            "Unable to load prediction history."
        )
        st.error(detail)

    except requests.exceptions.JSONDecodeError:
        st.error(
            f"Backend Error: {response.status_code}"
        )
        st.code(response.text)

    st.stop()


# Display Table
st.dataframe(
    history,
    use_container_width=True,
    hide_index=True)

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
        "🏡 Predict House Price",
        use_container_width=True
    ):
        st.switch_page("pages/FE7_House_Prediction.py")
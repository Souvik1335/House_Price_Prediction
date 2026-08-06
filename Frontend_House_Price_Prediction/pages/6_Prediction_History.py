import streamlit as st
from api import get_prediction_history


st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)


st.title("📜 Prediction History")


if "access_token" not in st.session_state:

    st.warning("Please login first.")

    st.switch_page(
        "pages/3_login.py"
    )


access_token = st.session_state["access_token"]


response = get_prediction_history(
    access_token
)


if isinstance(response, Exception):

    st.error(
        f"Connection Error: {response}"
    )


elif response.status_code == 200:

    data = response.json()

    history = data["history"]


    if len(history) == 0:

        st.info(
            "No predictions found."
        )


    else:

        for item in history:

            st.divider()

            st.write(
                f"🏠 Area: {item[0]} sqft"
            )

            st.write(
                f"🛏 Bedrooms: {item[1]}"
            )

            st.write(
                f"🚿 Bathrooms: {item[2]}"
            )

            st.write(
                f"🏢 Floors: {item[3]}"
            )

            st.write(
                f"📅 Age: {item[4]} years"
            )

            st.write(
                f"💰 Price: ₹ {item[5]:,.2f}"
            )

            st.write(
                f"⏰ Date: {item[6]}"
            )


else:

    st.error(
        response.json()["detail"]
    )
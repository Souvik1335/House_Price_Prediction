import streamlit as st
from utils.api import get_prediction
import requests

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered")


# Login Check
if "token" not in st.session_state:
    st.session_state.token = None

if st.session_state.token is None:
    st.warning("Please login first.")
    st.switch_page("pages/FE3_Login.py")


# Title
st.title("🏠 House Price Prediction")

st.write(
    "Enter the details below to predict the estimated house price."
)

st.divider()


# Prediction Form
with st.form("prediction_form"):

    area_sqft = st.number_input(
        "📐 Area (sqft)",
        min_value=100,
        value=1000,
        step=50)

    bedrooms = st.number_input(
        "🛏 Bedrooms",
        min_value=1,
        max_value=20,
        value=3)

    bathrooms = st.number_input(
        "🚿 Bathrooms",
        min_value=1,
        max_value=20,
        value=2)

    floors = st.number_input(
        "🏢 Floors",
        min_value=1,
        max_value=10,
        value=1)

    age_of_house = st.number_input(
        "🏚 Age of House (Years)",
        min_value=0,
        value=5)

    garage = st.selectbox(
        "🚗 Garage",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No")

    location_score = st.slider(
        "📍 Location Score",
        min_value=0,
        max_value=10,
        value=5)

    distance_to_city = st.number_input(
        "🏙 Distance to City (km)",
        min_value=0.0,
        value=5.0,
        step=0.5)

    school_rating = st.slider(
        "🏫 School Rating",
        min_value=0,
        max_value=10,
        value=5)

    crime_rate = st.slider(
        "🚨 Crime Rate",
        min_value=0,
        max_value=10,
        value=3)

    predict = st.form_submit_button(
        "🏠 Predict Price",
        use_container_width=True)


# Prediction
if predict:

    input_data = {
        "Area_sqft": area_sqft,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Floors": floors,
        "Age_of_House": age_of_house,
        "Garage": garage,
        "Location_Score": location_score,
        "Distance_to_City": distance_to_city,
        "School_Rating": school_rating,
        "Crime_Rate": crime_rate
    }

    st.write("### Input Data")
    st.json(input_data)

    with st.spinner("Predicting..."):
        response = get_prediction(
        token=st.session_state.token,
        house_data=input_data)

        if response.status_code == 200:
            result = response.json()

            predicted_price = result["predicted_price"]

            st.success("Prediction Completed!")

            st.metric(
            "Estimated House Price",
            f"₹ {predicted_price:,.0f}")

        
        else:
            try:
                detail = response.json().get(
                    "detail",
                    "Prediction failed."
                )
                st.error(detail)

            except requests.exceptions.JSONDecodeError:
                st.error(
                    f"Backend Error: {response.status_code}"
                )
                st.code(response.text)
        

st.divider()

col1, col2 = st.columns(2)
with col1:
    if st.button("🏠 Dashboard", use_container_width=True):
        st.switch_page("pages/FE5_Dashboard.py")

with col2:
    if st.button("📜 Prediction History", use_container_width=True):
        st.switch_page("pages/FE8_Prediction_History.py")
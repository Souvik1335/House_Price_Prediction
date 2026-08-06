import streamlit as st
from api import predict_house_price

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction Dashboard")

st.caption("Predict house prices using our Machine Learning model.")

# Authentication Check
if "access_token" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/3_login.py")


# Property Details of House
st.subheader("📐 Property Details")
col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "Area (sqft)",
        min_value=500,
        max_value=10000,
        value=1500
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

with col2:

    floors = st.number_input(
        "Floors",
        min_value=1,
        max_value=5,
        value=2
    )

    garage = st.selectbox(
        "Garage",
        [0, 1]
    )


# Location Details of the House
st.divider()
st.subheader("📍 Location Details")

col1, col2 = st.columns(2)

with col1:

    location_score = st.slider(
        "Location Score",
        min_value=1,
        max_value=10,
        value=5
    )

    school_rating = st.slider(
        "School Rating",
        min_value=1,
        max_value=10,
        value=5
    )

with col2:

    distance_to_city = st.number_input(
        "Distance to City (km)",
        min_value=0.0,
        max_value=100.0,
        value=10.0,
        step=0.5
    )

    crime_rate = st.slider(
        "Crime Rate",
        min_value=1,
        max_value=10,
        value=5
    )

#Age of the House
st.divider()
st.subheader("🏡 House Information")

age_of_house = st.number_input(
    "Age of House (Years)",
    min_value=0,
    max_value=100,
    value=10
)

# House Price Prediction
st.divider()

if st.button("🔮 Predict House Price", use_container_width=True):

    access_token = st.session_state["access_token"]

    data = {

        "Area_sqft": area,
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

    with st.spinner("Predicting House Price..."):

        response = predict_house_price(
            data,
            access_token
        )

        if isinstance(response, Exception):

            st.error(f"Connection Error: {response}")

        elif response.status_code == 200:

            result = response.json()

            st.metric(label="💰 Predicted House Price",value=f"₹ {result['predicted_price']:,.2f}")

        else:

            st.error(response.json()["detail"])
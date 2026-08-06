import streamlit as st
from api import get_profile

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="centered"
)

st.title("👤 My Profile")


if "access_token" not in st.session_state:
    st.warning("Please login first.")
    st.switch_page("pages/3_Login.py")
st.success("Login Successful!")


access_token = st.session_state["access_token"]
response = get_profile(access_token)


if isinstance(response, Exception):
    st.error(f"Connection Error: {response}")
elif response.status_code == 200:

    profile = response.json()

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Full Name**")
        st.write(profile["name"])

        st.write("**Phone**")
        st.write(profile["phone"])

        st.write("**Date of Birth**")
        st.write(profile["date_of_birth"])

    with col2:
        st.write("**Email**")
        st.write(profile["email"])

        st.write("**Alternate Phone**")
        st.write(profile["alternate_phone_number"])

    st.divider()

    st.subheader("💳 Payment Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Payment Type", profile["payment_type"])

    with col2:
        st.metric("EMI Years", profile["emi_years"])

    with col3:
        st.metric("Interest Rate", f"{profile['interest_rate']}%")

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):

        st.session_state.clear()

        st.switch_page("pages/3_Login.py")
else:
    st.error(response.json()["detail"])
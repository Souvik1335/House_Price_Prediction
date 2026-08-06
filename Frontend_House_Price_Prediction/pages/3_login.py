import streamlit as st
from api import login_user


st.set_page_config(
    page_title="Login",
    page_icon="🔑",
    layout="centered"
)


st.title("🔑 Login")

st.caption("Login to your account")


email = st.text_input(
    "Email Address"
)


password = st.text_input(
    "Password",
    type="password"
)


if st.button(
    "Login",
    use_container_width=True
):

    if not email or not password:

        st.error(
            "Please enter Email and Password."
        )

    else:

        response = login_user(
            email,
            password
        )


        if isinstance(response, Exception):

            st.error(
                f"Connection Error: {response}"
            )


        elif response.status_code == 200:

            data = response.json()


            st.session_state["access_token"] = data["access_token"]

            st.session_state["refresh_token"] = data["refresh_token"]

            st.session_state["email"] = email


            st.success(
                "Login Successful!"
            )


            st.switch_page(
                "pages/4_Profile.py"
            )


        else:

            st.error(
                response.json()["detail"]
            )
            
st.divider()

if st.button(
    "🔐 Forgot Password?",
    use_container_width=True
):

    st.switch_page(
        "pages/6_Reset_Password.py"
    )
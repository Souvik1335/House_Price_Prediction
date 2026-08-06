import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from api import verify_email


st.title("📧 Email Verification")


email = st.session_state.get("email")


if email:

    st.write(
        f"OTP sent to {email}"
    )


    otp = st.text_input(
        "Enter OTP"
    )


    if st.button("Verify"):

        data = {

            "email": email,
            "otp": otp

        }


        response = verify_email(data)


        if response.status_code == 200:

            st.success(
                "Email Verified Successfully!"
            )

            st.switch_page(
                "pages/3_login.py"
            )


        else:

            st.error(
                response.json()
            )

else:

    st.warning(
        "Please register first."
    )
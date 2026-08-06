import streamlit as st

from api import (
    forgot_password,
    reset_password
)


st.set_page_config(
    page_title="Reset Password",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Reset Password")

# -----------------------------
# Session State
# -----------------------------
if "reset_email" not in st.session_state:
    st.session_state["reset_email"] = ""

if "otp_sent" not in st.session_state:
    st.session_state["otp_sent"] = False

# -----------------------------
# Step 1 : Send OTP
# -----------------------------
st.subheader("Step 1 : Send OTP")

email = st.text_input(
    "Registered Email",
    value=st.session_state["reset_email"]
)

if st.button(
    "Send OTP",
    use_container_width=True
):

    if not email:

        st.error("Please enter your email.")

    else:

        response = forgot_password(email)

        if isinstance(response, Exception):

            st.error(
                f"Connection Error : {response}"
            )

        elif response.status_code == 200:

            st.session_state["reset_email"] = email
            st.session_state["otp_sent"] = True

            st.success(
                "OTP has been sent to your email."
            )

        else:

            st.error(
                response.json()["detail"]
            )

# -----------------------------
# Step 2 : Reset Password
# -----------------------------
if st.session_state["otp_sent"]:

    st.divider()

    st.subheader("Step 2 : Reset Password")

    otp = st.text_input(
        "OTP"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button(
        "Reset Password",
        use_container_width=True
    ):

        if not otp or not new_password or not confirm_password:

            st.error(
                "Please fill all fields."
            )

        elif new_password != confirm_password:

            st.error(
                "Passwords do not match."
            )

        else:

            response = reset_password(
                {
                    "email": st.session_state["reset_email"],
                    "otp": otp.strip(),
                    "new_password": new_password
                }
            )

            if isinstance(response, Exception):

                st.error(
                    f"Connection Error : {response}"
                )

            elif response.status_code == 200:

                st.success(
                    "Password reset successful!"
                )

                st.session_state["otp_sent"] = False
                st.session_state["reset_email"] = ""

                st.switch_page(
                    "pages/3_login.py"
                )

            else:

                try:

                    st.error(
                        response.json()["detail"]
                    )

                except:

                    st.error(response.text)

st.divider()

if st.button(
    "⬅ Back to Login",
    use_container_width=True
):

    st.switch_page(
        "pages/3_login.py"
    )
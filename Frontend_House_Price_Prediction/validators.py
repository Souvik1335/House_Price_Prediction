import re



# User Password Validation
def validate_password(password):
 
    if len(password) < 8:
        return False, "Password must contain at least 8 characters."
 
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain one uppercase letter."
 
    if not re.search(r"[a-z]", password):
        return False, "Password must contain one lowercase letter."
 
    if not re.search(r"[0-9]", password):
        return False, "Password must contain one digit."
 
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain one special character."
 
    return True, "Strong Password"
 
# User Email Validation
def validate_email(email):
 
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
 
    if re.match(pattern, email):
        return True
 
    return False
 
# User Phone Number Validation
def validate_phone(phone):
 
    pattern = r"^[6-9]\d{9}$"
 
    if re.match(pattern, phone):
        return True
 
    return False
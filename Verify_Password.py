import bcrypt

# User enters password during registration
password = input("Enter Your Password :- ")

# Convert to bytes
password_bytes = password.encode("utf-8")

# Hash the password
hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print("\nPassword Stored Successfully!")

print("\nNow Login")

# User enters password again
login_password = input("Enter Password: ")

# Convert login password to bytes
login_password_bytes = login_password.encode("utf-8")

# Verify password
if bcrypt.checkpw(login_password_bytes, hashed_password):
    print("\n Login Successful")
else:
    print("\n Incorrect Password")
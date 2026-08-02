import bcrypt

password = input('Enter Your Password :- ')

# Convert string to bytes
password_bytes = password.encode("utf-8")

# Generate Salt
salt = bcrypt.gensalt()

# Hash Password
hashed_password = bcrypt.hashpw(password_bytes, salt)

print("\nOriginal Password :", password)
print("Hashed Password   :", hashed_password.decode("utf-8"))
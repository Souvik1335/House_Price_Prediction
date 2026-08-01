import sqlite3

connection = sqlite3.connect('User_Database.db')

cursor = connection.cursor()

# User Input
email = input("Enter Your Email: ")

# Delete Query
cursor.execute("""
DELETE FROM User_Database
WHERE email = ?
""", (email,))

# Save Changes
connection.commit()

# Check whether user was deleted
if cursor.rowcount > 0:
    print("User Deleted Successfully.")
else:
    print("User Not Found.")

# Close Database
connection.close()
import sqlite3

connection = sqlite3.connect('User_Database.db')

cursor = connection.cursor()

#User Input
email = input("Enter your Email :- ")
new_interest_rate = float(input("Enter your Interest rate :- "))

#Update User Data
# Update Query
cursor.execute("""
UPDATE User_Database
SET interest_rate = ?
WHERE email = ?
""", (new_interest_rate, email))

connection.commit()

# Check Update
if cursor.rowcount > 0:
    print("User Updated Successfully")
else:
    print("User Not Found")

# Close Database
connection.close()
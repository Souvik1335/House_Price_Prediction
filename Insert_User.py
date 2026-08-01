import sqlite3

connection = sqlite3.connect('User_Database.db')

cursor = connection.cursor()

cursor.execute("""
INSERT INTO User_Database
(name, email, phone, password, Date_of_Birth, alternet_phone_number, paayment_type, emi_years, 
interest_rate)

VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    'Souvik Banerjee',
    'souvikbanerjee@gmail.com',
    '8918667515',
    'Souvik@2005',
    '13/03/2005',
    '7866166611',
    'EMI',
    10,
    20.0
))

connection.commit()
connection.close()

print("User Insert Successfully")
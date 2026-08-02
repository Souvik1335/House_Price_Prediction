import sqlite3

connection = sqlite3.connect('User_Database.db')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS User_Database(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    phone TEXT UNIQUE,
    password TEXT,
    Date_of_Birth TEXT,
    alternate_phone_number TEXT,
    payment_type TEXT,
    emi_years INTEGER,
    interest_rate REAL,
    email_verified INTEGER DEFAULT 0,
    otp TEXT,
    otp_expiry TEXT
)
""")

connection.commit()
connection.close()

print("Database Created Successfully!")
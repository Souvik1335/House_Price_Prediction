import sqlite3

connection = sqlite3.connect('User_Database.db')

cursor = connection.cursor()

email = input('Enter Your Email :- ')

cursor.execute('SELECT * FROM User_Database WHERE email = ?', (email,))

user = cursor.fetchone()

if user:
    print('User Founded')
    print(user)
else:
    print('User not Found')

connection.close()
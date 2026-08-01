import sqlite3

connection = sqlite3.connect('User_Database.db')

cursor = connection.cursor()

cursor.execute('SELECT * FROM User_Database')

users = cursor.fetchall()

for user in users: 
    print(user)

connection.close()
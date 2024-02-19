import mysql.connector as connector

connection = connector.connect(host="localhost", user="root", password="python")

if connection.is_connected():
    print("Successfully connected!")
else:
    print("Failed connection!")
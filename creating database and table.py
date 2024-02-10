import mysql.connector as mysqlConnector

# connection = mysqlConnector.connect(host="localhost", user="root", password="<password>")  # connection without database

connection = mysqlConnector.connect(host="localhost", user="root", password="<password>", database="som")  # connection with database

if connection.is_connected():
    print("Successfully connected!")
else:
    print("Failed connection!")

cursor = connection.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS som")

cursor.execute("CREATE TABLE IF NOT EXISTS product(name VARCHAR(100), price INT)")
# cursor.execute("INSERT INTO product (name, price) VALUES('Mobile', 200)")
# connection.commit()
cursor.execute("SELECT * FROM product")
records = cursor.fetchall()
print(records)
cursor.close()
import mysql.connector as mysqlConnector

connection = mysqlConnector.connect(
    host="127.0.0.1", user="root", password="<password>"
)

if connection.is_connected():
    print("Successfully Connected!")
else:
    print("Failed connection!")

cursor = connection.cursor(dictionary=True)
cursor.execute("SHOW DATABASES")
DBS = cursor.fetchall()

for db in DBS:
    print(db["Database"])

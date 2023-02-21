import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Phani$28896"
)
if mydb:
    print("connected")
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
print()
mycursor.execute("DROP DATABASE IF EXISTS mydatabase")
mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
print()

# mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")


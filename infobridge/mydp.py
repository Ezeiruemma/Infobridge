import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Chibeks999',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE info")

print("ALL Done!")
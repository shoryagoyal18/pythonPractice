import mysql.connector
 
connectionObject = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "$horya"
)

print(connectionObject)

cursor = connectionObject.cursor()

cursor.execute("create database pythonPractice")
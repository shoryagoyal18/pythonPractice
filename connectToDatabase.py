import mysql.connector
 
connectionObject = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "$horya", 
    database = 'pythonPractice'
)

print(connectionObject)

cursor = connectionObject.cursor()

# Creating databases 
#cursor.execute("create database pythonPractice")

# Creating a table
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   INCOME FLOAT
)'''
cursor.execute(sql)
# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='admin123',
    auth_plugin='mysql_native_password'
    
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")

dataBase.close()

# import mysql.connector
# conn = mysql.connector.connect(host='localhost', password='admin123', user='root')

# if conn.is_connected():
#     print("connection is successfull")
    
    
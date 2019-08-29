
from datetime import date, datetime, timedelta
import mysql.connector

mydb = mysql.connector.connect(user='root', password='02070',
                              host='127.0.0.1', database='schroniskov2')
cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)



import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='wsaa'
)

cur =mydb.cursor()
sql = '''
    CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(225),
    age INT
)
'''

cur.execute(sql)

cur.close()
mydb.close()
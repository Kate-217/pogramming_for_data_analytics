import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

# to get all rows
result = cur.execute('SELECT * FROM book2')
print(result.fetchall())

# another way to get all rows
for row in cur.execute('SELECT * from book2'):
    print(f'row: {row}')


# to get UNIQUE values: 
for row in cur.execute('SELECT DISTINCT ISBN, title, author FROM book2'):
    print(f'Row: {row}')
import sqlite3
con = sqlite3.connect('pfda.db') 
cur = con.cursor() # creating an object cursor

# This will not work, because there is nothing in the book2 yet.

#result = cur.execute("SELECT * FROM book2")# checking what is in the DB
#print (result.fetchone()) # show the first row from the result

#insert a book

sql = """
    INSERT INTO book2 VALUES
    ('The Brothers Karamazov','F.M. Dostoevsky','123'),
    ('Idiot','F.M. Dostoevsky', '124')
"""
cur.execute(sql)
con.commit() # to save changes

# checking the data
result = cur.execute("SELECT * FROM book2")
print(result.fetchone()) # returns one row

# closing the connection to the database in SQLite
con.close()
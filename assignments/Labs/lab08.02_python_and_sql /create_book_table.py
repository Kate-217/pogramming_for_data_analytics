import sqlite3

# connecting to BD
con = sqlite3.connect('pfda.db')

# A cursor is a mechanism for sending queries 
# to a database and retrieving results.
cur = con.cursor()

cur.execute("CREATE TABLE book2 (title TEXT, author TEXT, ISBN TEXT)")

# closing the connection to the database in SQLite
con.close()

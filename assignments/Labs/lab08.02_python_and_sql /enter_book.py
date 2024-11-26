import sqlite3
con = sqlite3.connect('pfda.db')
cur = con.cursor()

#creating an empty dictionary:
book = {}
book['title'] = input('Please, enter book title: ')
book['author'] = input('Please, enter book author: ')
book['ISBN'] = input('Please, enter book ISBN: ')

#The inputs are stored
# in the corresponding keys of the dictionary book

data = [book] #The book dictionary is added to a list called data.

#Named placeholders (:title, :author, :ISBN) are used for
# the values, ensuring safety from SQL injection.
sql = "INSERT into book values (:title, :author, :ISBN)"

#The executemany method executes the SQL query 
#for every dictionary in the data list.
cur.executemany(sql,data)
con.commit()

for row in cur.execute('SELECT * FROM book'):
    print(f"row{row}")
import sqlite3
from tabulate import tabulate
conn=sqlite3.connect("database/books.db")
c=conn.cursor()
def creatdatabase():
    global conn
    global c
    c.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT COLLATE NOCASE,
        author TEXT COLLATE NOCASE,
        publish_year INTEGER
    )
    ''')
    conn.commit()
    #conn.close()
def showallbook():
    c.execute("SELECT * FROM books")
    print(tabulate(c.fetchall(),headers=["id","name","author","year"],tablefmt="fancy_grid"))
    conn.commit()
    #c.close()
def searchbyname(name):
    c.execute("SELECT * FROM books WHERE name=? LIMIT 1",(name,))
    if c.fetchone():
        c.execute("SELECT * FROM books WHERE name=?",(name,))
        print(tabulate(c.fetchall(),headers=["id","name","author","year"],tablefmt="fancy_grid"))
    else:
        print("Your bookname could not be found")
    conn.commit()
    #c.close()
def searchbyid(id1):
    c.execute("SELECT * FROM books WHERE id=? LIMIT 1",(id1,))
    if c.fetchone():
        c.execute("SELECT * FROM books WHERE id=?",(id1,))
        print(tabulate(c.fetchall(),headers=["id","name","author","year"],tablefmt="fancy_grid"))
        conn.commit()
        #c.close()
    else:
        print("Your id could not be found")
def searchbyauthor(author):
    c.execute("SELECT * FROM books WHERE author=? LIMIT 1",(author,))
    if c.fetchone():
        c.execute("SELECT * FROM books WHERE author=?",(author,))
        print(tabulate(c.fetchall(),headers=["id","name","author","year"],tablefmt="fancy_grid"))
        conn.commit()
        #c.close()
    else:
        print("Your author could not be found")
def add(name,author,publish_year):
    c.execute("INSERT into books values(?,?,?,?)",(None,name,author,publish_year))
    c.execute("SELECT * FROM books WHERE name=? AND author=? AND publish_year=?",(name,author,publish_year))
    print("ketab be database ezafe shod!")
    print("your information : ")
    print(tabulate(c.fetchall(),headers=["id","name","author","year"],tablefmt="fancy_grid"))
    conn.commit()
    #c.close()
def remove(name,author,publish_year):
    c.execute("SELECT * from books WHERE name=? AND author=? AND publish_year=?",(name,author,publish_year))
    if c.fetchone():
        c.execute("DELETE from books WHERE name=? AND author=? AND publish_year=?",(name,author,publish_year))
        print("book was removed succesfully!")
        conn.commit()
        #c.close()
    else:
        print("Your book could not be found")
def recognizebook(id):
    c.execute("SELECT * FROM books WHERE id=?",(id,))
    if c.fetchone():
        return True
    else:
        return False
def foundnameofbook(id):
    c.execute("SELECT name FROM books WHERE id=?",(id,))
    bookname=c.fetchall()
    bookname=bookname[0][0]
    return bookname